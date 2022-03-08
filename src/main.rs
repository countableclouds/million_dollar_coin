use rand::{rngs::ThreadRng, thread_rng, Rng};
use std::collections::HashMap;

fn score(f: impl Fn(usize) -> usize, iterations: usize) -> f64 {
    let mut probabilities: Vec<f64> = Vec::with_capacity(iterations);
    probabilities.push(0.5);

    // We assume that the number of counts never rises above 2 * iterations,
    // because doing so would mean that the beneficial strategy involves
    // many absorbing points much much higher than half (unlikely)
    let mut counts: Vec<f64> = Vec::with_capacity(2 * iterations);
    counts.push(0.5);

    // Base case
    let mut f_i_ = f(0);
    let mut f_i: usize;
    assert!(
        f_i_ == 1,
        "This function cannot be optimal because f(0) != 1!"
    );

    // Get the partial sums of the numbers
    for i in 1..iterations {
        f_i = f(i);
        let df = (f_i - f_i_ + 1).try_into().unwrap();
        // df + 1. The difference between the two f's tells us how many levels down we dropped, plus an
        // additional level due to the indexing of the chain. Therefore, we have dropped 2^(df+1), and so we
        // scale down by that.
        counts.iter_mut().for_each(|c| *c /= 2_u32.pow(df) as f64);

        f_i_ = f_i;
        for j in 1..counts.len().min(f_i) {
            counts[j] += counts[j - 1];
        }

        counts.extend(vec![counts[counts.len() - 1]; f_i - counts.len()]);
        probabilities.push(counts[counts.len() - 1])
    }

    let values: Vec<f64> = (0..iterations)
        .map(|i| {
            let f_i = f(i) as f64;
            f_i / (i as f64 + f_i)
        })
        .collect();

    let init_sum: f64 = probabilities.iter().zip(values).map(|(p, v)| p * v).sum();
    let total_probability: f64 = probabilities.iter().sum();

    init_sum + (1. - total_probability) * 0.5
}

fn augmented_strategy(custom: HashMap<usize, usize>) -> impl (Fn(usize) -> usize) {
    move |x| *custom.get(&x).unwrap_or(&(x + 1))
}

fn random_strategy(
    optimizer: usize,
    max_test: usize,
    rng: &mut ThreadRng,
) -> HashMap<usize, usize> {
    let mut runner: usize = 1;
    let mut custom: HashMap<usize, usize> = HashMap::new();
    for i in 1..optimizer {
        if runner == i {
            runner += rng.gen_range(1..max_test);
        } else {
            runner += rng.gen_range(0..max_test);
        }
        custom.insert(i, runner);
    }
    for j in optimizer..runner {
        custom.insert(j, runner);
    }
    custom
}

fn main() {
    let mut rng = thread_rng();
    // 500:  0.000001 accuracy  in 0.387 ms
    // 100:  0.00004 accuracy in 0.02 ms
    let iterations: usize = 100;
    let mut max_custom: HashMap<usize, usize> = HashMap::new();
    let mut max_score = 0.;
    // let s = score(augmented_strategy(custom), iterations);
    for _ in 0..10000000 {
        let custom = random_strategy(30, 5, &mut rng);
        let s = score(augmented_strategy(custom.clone()), iterations);
        if s > max_score {
            max_score = s;
            max_custom = custom;
        }
    }
    let mut values: Vec<(usize, usize)> = max_custom.iter().map(|(a, b)| (*a, *b)).collect();
    values.sort_by(|(a, _), (b, _)| a.cmp(b));
    values = values.iter().map(|(a, b)| (*b, (*a + *b))).collect();
    println!("{}: {:?}", max_score, values);

    // let s = score(
    //     |n| {
    //         if n > 0 {
    //             n + 2
    //         } else {
    //             n + 1
    //         }
    //     },
    //     iterations,
    // );
    // println!("The score is {}!", s);
}
