use rand::{rngs::ThreadRng, thread_rng, Rng};
use std::collections::HashMap;
use std::{thread, time};

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

fn augmented_strategy<'a>(custom: &'a HashMap<usize, usize>) -> impl (Fn(usize) -> usize) + 'a {
    move |x| custom.get(&x).copied().unwrap_or(x + 1)
}

fn to_string(i: usize, f: impl (Fn(usize) -> usize)) -> String {
    (0..i)
        .map(|n| format!("({}: {})", n, f(n)))
        .collect::<Vec<String>>()
        .join(", ")
}

fn main() {
    let mut rng = thread_rng();
    // 500:  0.000001 accuracy  in 0.387 ms
    // 100:  0.00004 accuracy in 0.02 ms
    let mut counter = 0;
    let mut strategy: HashMap<usize, usize> = HashMap::new();
    let mut best_score = score(augmented_strategy(&strategy), 100);
    let iterations = 400;
    let mut level = iterations;
    loop {
        if counter % 10000 == 0 {
            println!(
                "Score: {}\nStrategy: {}\n",
                best_score,
                to_string(20, augmented_strategy(&strategy))
            )
        }

        counter += 1;
        level -= 1;
        // thread::sleep(time::Duration::from_millis(10));

        if strategy.get(&level).unwrap_or(&(level + 1))
            == strategy.get(&(level + 1)).unwrap_or(&(level + 2))
        {
            continue;
        }

        strategy.insert(level, strategy.get(&level).unwrap_or(&(level + 1)) + 1);

        let new_score = score(augmented_strategy(&strategy), iterations);
        if new_score > best_score {
            best_score = new_score;
            level += 1;
        } else {
            strategy.insert(level, strategy.get(&level).unwrap() - 1);
        }

        if level == 1 {
            println!("Fully optimized!");
            println!(
                "Score: {}\nStrategy: {}\n",
                best_score,
                to_string(iterations, augmented_strategy(&strategy))
            );
            break;
        }
    }
}
