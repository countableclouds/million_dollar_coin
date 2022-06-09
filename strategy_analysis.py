import numpy as np
import matplotlib.pyplot as plt

down_top = "(0: 1), (1: 3), (2: 4), (3: 5), (4: 7), (5: 8), (6: 9), (7: 11), (8: 12), (9: 13), (10: 14), (11: 15), (12: 16), (13: 18), (14: 19), (15: 20), (16: 21), (17: 22), (18: 23), (19: 25), (20: 26), (21: 27), (22: 28), (23: 29), (24: 30), (25: 31), (26: 32), (27: 34), (28: 35), (29: 36), (30: 37), (31: 38), (32: 39), (33: 40), (34: 41), (35: 42), (36: 43), (37: 45), (38: 46), (39: 47), (40: 48), (41: 49), (42: 50), (43: 51), (44: 52), (45: 53), (46: 54), (47: 55), (48: 57), (49: 58), (50: 59), (51: 60), (52: 61), (53: 62), (54: 63), (55: 64), (56: 65), (57: 66), (58: 67), (59: 68), (60: 69), (61: 71), (62: 72), (63: 73), (64: 74), (65: 75), (66: 76), (67: 77), (68: 78), (69: 79), (70: 80), (71: 81), (72: 82), (73: 83), (74: 84), (75: 85), (76: 87), (77: 88), (78: 89), (79: 90), (80: 91), (81: 92), (82: 93), (83: 94), (84: 95), (85: 96), (86: 97), (87: 98), (88: 99), (89: 100), (90: 101), (91: 102), (92: 104), (93: 105), (94: 106), (95: 107), (96: 108), (97: 109), (98: 110), (99: 111), (100: 112), (101: 113), (102: 114), (103: 115), (104: 116), (105: 117), (106: 118), (107: 119), (108: 120), (109: 121), (110: 123), (111: 124), (112: 125), (113: 126), (114: 127), (115: 128), (116: 129), (117: 130), (118: 131), (119: 132), (120: 133), (121: 134), (122: 135), (123: 136), (124: 137), (125: 138), (126: 139), (127: 140), (128: 141), (129: 142), (130: 144), (131: 145), (132: 146), (133: 147), (134: 148), (135: 149), (136: 150), (137: 151), (138: 152), (139: 153), (140: 154), (141: 155), (142: 156), (143: 157), (144: 158), (145: 159), (146: 160), (147: 161), (148: 162), (149: 163), (150: 164), (151: 166), (152: 167), (153: 168), (154: 169), (155: 170), (156: 171), (157: 172), (158: 173), (159: 174), (160: 175), (161: 176), (162: 177), (163: 178), (164: 179), (165: 180), (166: 181), (167: 182), (168: 183), (169: 184), (170: 185), (171: 186), (172: 187), (173: 188), (174: 189), (175: 191), (176: 192), (177: 193), (178: 194), (179: 195), (180: 196), (181: 197), (182: 198), (183: 199), (184: 200), (185: 201), (186: 202), (187: 203), (188: 204), (189: 205), (190: 206), (191: 207), (192: 208), (193: 209), (194: 210), (195: 211), (196: 212), (197: 213), (198: 214), (199: 215), (200: 217), (201: 218), (202: 219), (203: 220), (204: 221), (205: 222), (206: 223), (207: 224), (208: 225), (209: 226), (210: 227), (211: 228), (212: 229), (213: 230), (214: 231), (215: 232), (216: 233), (217: 234), (218: 235), (219: 236), (220: 237), (221: 238), (222: 239), (223: 240), (224: 241), (225: 242), (226: 243), (227: 244), (228: 246), (229: 247), (230: 248), (231: 249), (232: 250), (233: 251), (234: 252), (235: 253), (236: 254), (237: 255), (238: 256), (239: 257), (240: 258), (241: 259), (242: 260), (243: 261), (244: 262), (245: 263), (246: 264), (247: 265), (248: 266), (249: 267), (250: 268), (251: 269), (252: 271), (253: 271), (254: 272), (255: 273), (256: 275), (257: 275), (258: 276), (259: 277), (260: 279), (261: 280), (262: 281), (263: 282), (264: 283), (265: 284), (266: 285), (267: 286), (268: 287), (269: 288), (270: 289), (271: 290), (272: 291), (273: 292), (274: 293), (275: 294), (276: 295), (277: 296), (278: 297), (279: 298), (280: 299), (281: 300), (282: 302), (283: 302), (284: 303), (285: 305), (286: 305), (287: 306), (288: 307), (289: 308), (290: 309), (291: 311), (292: 311), (293: 313), (294: 313), (295: 314), (296: 316), (297: 317), (298: 318), (299: 319), (300: 320), (301: 321), (302: 322), (303: 323), (304: 324), (305: 325), (306: 326), (307: 328), (308: 328), (309: 329), (310: 330), (311: 331), (312: 332), (313: 333), (314: 335), (315: 336), (316: 336), (317: 337), (318: 338), (319: 339), (320: 341), (321: 341), (322: 343), (323: 343), (324: 344), (325: 346), (326: 346), (327: 347), (328: 348), (329: 349), (330: 351), (331: 351), (332: 352), (333: 354), (334: 355), (335: 355), (336: 358), (337: 358), (338: 358), (339: 361), (340: 361), (341: 362), (342: 364), (343: 365), (344: 366), (345: 366), (346: 367), (347: 368), (348: 370), (349: 370), (350: 372), (351: 372), (352: 373), (353: 373), (354: 374), (355: 376), (356: 377), (357: 378), (358: 380), (359: 380), (360: 380), (361: 382), (362: 383), (363: 385), (364: 385), (365: 386), (366: 387), (367: 389), (368: 389), (369: 389), (370: 390), (371: 391), (372: 394), (373: 394), (374: 395), (375: 396), (376: 397), (377: 399), (378: 399), (379: 401), (380: 401), (381: 402), (382: 403), (383: 405), (384: 405), (385: 406), (386: 408), (387: 409), (388: 409), (389: 411), (390: 411), (391: 412), (392: 413), (393: 415), (394: 415), (395: 417), (396: 418), (397: 418), (398: 418), (399: 422), (400: 422), (401: 422), (402: 423), (403: 425), (404: 426), (405: 427), (406: 427), (407: 429), (408: 429), (409: 430), (410: 431), (411: 433), (412: 433), (413: 434), (414: 435), (415: 436), (416: 439), (417: 439), (418: 442), (419: 442), (420: 443), (421: 443), (422: 443), (423: 444), (424: 446), (425: 448), (426: 449), (427: 449), (428: 449), (429: 451), (430: 451), (431: 452), (432: 455), (433: 455), (434: 455), (435: 458), (436: 458), (437: 459), (438: 461), (439: 461), (440: 463), (441: 463), (442: 463), (443: 464), (444: 466), (445: 466), (446: 468), (447: 469), (448: 471), (449: 473), (450: 473), (451: 473), (452: 474), (453: 475), (454: 475), (455: 476), (456: 477), (457: 479), (458: 479), (459: 483), (460: 483), (461: 484), (462: 485), (463: 485), (464: 485), (465: 487), (466: 488), (467: 489), (468: 489), (469: 491), (470: 492), (471: 493), (472: 494), (473: 495), (474: 496), (475: 496), (476: 497), (477: 498), (478: 501), (479: 501), (480: 501), (481: 502), (482: 504), (483: 506), (484: 506), (485: 507), (486: 508), (487: 508), (488: 511), (489: 511), (490: 511), (491: 513), (492: 514), (493: 514), (494: 516), (495: 517), (496: 517), (497: 519), (498: 519), (499: 523), (500: 523), (501: 524), (502: 524), (503: 526), (504: 526), (505: 526), (506: 528), (507: 530), (508: 530), (509: 532), (510: 533), (511: 533), (512: 533), (513: 535), (514: 536), (515: 538), (516: 538), (517: 538), (518: 540), (519: 542), (520: 542), (521: 542), (522: 544), (523: 545), (524: 545), (525: 547), (526: 548), (527: 549), (528: 551), (529: 552), (530: 552), (531: 552), (532: 554), (533: 554), (534: 556), (535: 557), (536: 558), (537: 559), (538: 559), (539: 560), (540: 562), (541: 563), (542: 564), (543: 565), (544: 565), (545: 567), (546: 569), (547: 569), (548: 569), (549: 570), (550: 574), (551: 574), (552: 575), (553: 576), (554: 576), (555: 576), (556: 579), (557: 579), (558: 579), (559: 581), (560: 582), (561: 583), (562: 584), (563: 584), (564: 585), (565: 588), (566: 588), (567: 588), (568: 591), (569: 591), (570: 591), (571: 594), (572: 594), (573: 594), (574: 595), (575: 597), (576: 597), (577: 600), (578: 600), (579: 600), (580: 602), (581: 602), (582: 604), (583: 605), (584: 606), (585: 607), (586: 608), (587: 610), (588: 610), (589: 612), (590: 612), (591: 615), (592: 615), (593: 615), (594: 615), (595: 617), (596: 617), (597: 618), (598: 621), (599: 621), (600: 621), (601: 624), (602: 625), (603: 625), (604: 626), (605: 627), (606: 628), (607: 628), (608: 630), (609: 630), (610: 632), (611: 633), (612: 633), (613: 635), (614: 635), (615: 637), (616: 637), (617: 639), (618: 639), (619: 640), (620: 642), (621: 642), (622: 642), (623: 645), (624: 646), (625: 647), (626: 648), (627: 648), (628: 650), (629: 653), (630: 653), (631: 654), (632: 654), (633: 654), (634: 656), (635: 656), (636: 659), (637: 660), (638: 660), (639: 662), (640: 663), (641: 663), (642: 663), (643: 664), (644: 666), (645: 666), (646: 667), (647: 667), (648: 669), (649: 672), (650: 672), (651: 672), (652: 672), (653: 674), (654: 676), (655: 676), (656: 676), (657: 678), (658: 681), (659: 681), (660: 682), (661: 682), (662: 683), (663: 684), (664: 685), (665: 687), (666: 687), (667: 689), (668: 690), (669: 692), (670: 692), (671: 692), (672: 693), (673: 694), (674: 695), (675: 697), (676: 699), (677: 699), (678: 699), (679: 699), (680: 700), (681: 702), (682: 702), (683: 705), (684: 705), (685: 707), (686: 707), (687: 709), (688: 710), (689: 710), (690: 710), (691: 712), (692: 715), (693: 715), (694: 716), (695: 716), (696: 717), (697: 719), (698: 719), (699: 720), (700: 721), (701: 721), (702: 723), (703: 723), (704: 726), (705: 728), (706: 729), (707: 730), (708: 730), (709: 730), (710: 731), (711: 731), (712: 733), (713: 735), (714: 736), (715: 736), (716: 737), (717: 738), (718: 738), (719: 740), (720: 741), (721: 743), (722: 743), (723: 745), (724: 747), (725: 747), (726: 748), (727: 750), (728: 751), (729: 751), (730: 752), (731: 752), (732: 753), (733: 754), (734: 756), (735: 756), (736: 759), (737: 759), (738: 759), (739: 761), (740: 762), (741: 762), (742: 763), (743: 764), (744: 765), (745: 766), (746: 767), (747: 769), (748: 769), (749: 770), (750: 771), (751: 773), (752: 773), (753: 774), (754: 776), (755: 776), (756: 778), (757: 778), (758: 778), (759: 782), (760: 782), (761: 783), (762: 783), (763: 784), (764: 785), (765: 787), (766: 787), (767: 789), (768: 789), (769: 790), (770: 791), (771: 792), (772: 792), (773: 795), (774: 795), (775: 797), (776: 798), (777: 798), (778: 798), (779: 801), (780: 801), (781: 803), (782: 803), (783: 804), (784: 805), (785: 806), (786: 808), (787: 808), (788: 809), (789: 811), (790: 811), (791: 813), (792: 813), (793: 813), (794: 815), (795: 816), (796: 817), (797: 818), (798: 819), (799: 820), (800: 820), (801: 821), (802: 823), (803: 825), (804: 825), (805: 825), (806: 827), (807: 827), (808: 829), (809: 829), (810: 831), (811: 832), (812: 834), (813: 834), (814: 837), (815: 838), (816: 838), (817: 838), (818: 838), (819: 841), (820: 841), (821: 841), (822: 842), (823: 844), (824: 845), (825: 848), (826: 848), (827: 848), (828: 851), (829: 851), (830: 851), (831: 852), (832: 854), (833: 854), (834: 854), (835: 855), (836: 858), (837: 858), (838: 859), (839: 859), (840: 860), (841: 862), (842: 864), (843: 865), (844: 865), (845: 866), (846: 868), (847: 868), (848: 868), (849: 871), (850: 872), (851: 872), (852: 873), (853: 873), (854: 876), (855: 876), (856: 876), (857: 878), (858: 880), (859: 880), (860: 881), (861: 882), (862: 882), (863: 883), (864: 884), (865: 886), (866: 886), (867: 887), (868: 890), (869: 891), (870: 891), (871: 893), (872: 893), (873: 894), (874: 895), (875: 895), (876: 898), (877: 898), (878: 898), (879: 901), (880: 901), (881: 903), (882: 903), (883: 905), (884: 905), (885: 905), (886: 906), (887: 908), (888: 908), (889: 910), (890: 912), (891: 912), (892: 913), (893: 913), (894: 917), (895: 917), (896: 917), (897: 918), (898: 919), (899: 921), (900: 921), (901: 923), (902: 923), (903: 924), (904: 924), (905: 926), (906: 928), (907: 928), (908: 931), (909: 931), (910: 931), (911: 933), (912: 933), (913: 933), (914: 934), (915: 937), (916: 937), (917: 937), (918: 941), (919: 941), (920: 941), (921: 941), (922: 943), (923: 943), (924: 945), (925: 946), (926: 947), (927: 948), (928: 949), (929: 951), (930: 951), (931: 951), (932: 952), (933: 953), (934: 956), (935: 957), (936: 957), (937: 958), (938: 958), (939: 961), (940: 962), (941: 962), (942: 963), (943: 964), (944: 965), (945: 967), (946: 967), (947: 968), (948: 968), (949: 969), (950: 971), (951: 973), (952: 973), (953: 974), (954: 975), (955: 977), (956: 977), (957: 977), (958: 980), (959: 980), (960: 982), (961: 982), (962: 984), (963: 985), (964: 986), (965: 986), (966: 987), (967: 988), (968: 990), (969: 990), (970: 991), (971: 991), (972: 993), (973: 994), (974: 996), (975: 996), (976: 997), (977: 999), (978: 999), (979: 999), (980: 1001), (981: 1002), (982: 1002), (983: 1004), (984: 1004), (985: 1006), (986: 1007), (987: 1009), (988: 1009), (989: 1009), (990: 1010), (991: 1011), (992: 1013), (993: 1016), (994: 1016), (995: 1016), (996: 1018), (997: 1019), (998: 1019), (999: 1019), (1000: 1020), (1001: 1023), (1002: 1023), (1003: 1025), (1004: 1025), (1005: 1026), (1006: 1026), (1007: 1029), (1008: 1030), (1009: 1030), (1010: 1030), (1011: 1033), (1012: 1033), (1013: 1034), (1014: 1036), (1015: 1036), (1016: 1038), (1017: 1039), (1018: 1040), (1019: 1040), (1020: 1042), (1021: 1043), (1022: 1045), (1023: 1045), (1024: 1046), (1025: 1046), (1026: 1047), (1027: 1048), (1028: 1050), (1029: 1050), (1030: 1051), (1031: 1051), (1032: 1053), (1033: 1056), (1034: 1056), (1035: 1056), (1036: 1058), (1037: 1058), (1038: 1058), (1039: 1060), (1040: 1063), (1041: 1063), (1042: 1065), (1043: 1065), (1044: 1065), (1045: 1065), (1046: 1066), (1047: 1067), (1048: 1069), (1049: 1071), (1050: 1071), (1051: 1071), (1052: 1075), (1053: 1075), (1054: 1076), (1055: 1077), (1056: 1077), (1057: 1078), (1058: 1080), (1059: 1081), (1060: 1081), (1061: 1082), (1062: 1084), (1063: 1084), (1064: 1085), (1065: 1087), (1066: 1088), (1067: 1088), (1068: 1088), (1069: 1090), (1070: 1091), (1071: 1093), (1072: 1093), (1073: 1096), (1074: 1096), (1075: 1097), (1076: 1098), (1077: 1098), (1078: 1098), (1079: 1099), (1080: 1100), (1081: 1101), (1082: 1104), (1083: 1105), (1084: 1106), (1085: 1106), (1086: 1106), (1087: 1109), (1088: 1109), (1089: 1109), (1090: 1110), (1091: 1111), (1092: 1114), (1093: 1114), (1094: 1115), (1095: 1117), (1096: 1117), (1097: 1118), (1098: 1119), (1099: 1119), (1100: 1120), (1101: 1121), (1102: 1123), (1103: 1125), (1104: 1125), (1105: 1125), (1106: 1129), (1107: 1130), (1108: 1130), (1109: 1130), (1110: 1131), (1111: 1131), (1112: 1132), (1113: 1134), (1114: 1135), (1115: 1135), (1116: 1136), (1117: 1136), (1118: 1139), (1119: 1140), (1120: 1141), (1121: 1143), (1122: 1143), (1123: 1144), (1124: 1144), (1125: 1145), (1126: 1146), (1127: 1148), (1128: 1150), (1129: 1150), (1130: 1151), (1131: 1152), (1132: 1153), (1133: 1153), (1134: 1155), (1135: 1157), (1136: 1158), (1137: 1158), (1138: 1158), (1139: 1159), (1140: 1159), (1141: 1161), (1142: 1163), (1143: 1164), (1144: 1164), (1145: 1165), (1146: 1166), (1147: 1168), (1148: 1170), (1149: 1170), (1150: 1171), (1151: 1172), (1152: 1172), (1153: 1173), (1154: 1175), (1155: 1175), (1156: 1175), (1157: 1178), (1158: 1178), (1159: 1179), (1160: 1180), (1161: 1181), (1162: 1184), (1163: 1184), (1164: 1184), (1165: 1184), (1166: 1187), (1167: 1188), (1168: 1189), (1169: 1189), (1170: 1190), (1171: 1192), (1172: 1192), (1173: 1192), (1174: 1195), (1175: 1195), (1176: 1197), (1177: 1198), (1178: 1198), (1179: 1200), (1180: 1200), (1181: 1201), (1182: 1202), (1183: 1205), (1184: 1205), (1185: 1206), (1186: 1207), (1187: 1209), (1188: 1209), (1189: 1210), (1190: 1210), (1191: 1211), (1192: 1214), (1193: 1215), (1194: 1215), (1195: 1216), (1196: 1217), (1197: 1218), (1198: 1219), (1199: 1220), (1200: 1221), (1201: 1223), (1202: 1223), (1203: 1223), (1204: 1224), (1205: 1227), (1206: 1227), (1207: 1228), (1208: 1228), (1209: 1230), (1210: 1232), (1211: 1232), (1212: 1233), (1213: 1234), (1214: 1234), (1215: 1236), (1216: 1237), (1217: 1237), (1218: 1239), (1219: 1240), (1220: 1241), (1221: 1241), (1222: 1244), (1223: 1244), (1224: 1247), (1225: 1247), (1226: 1247), (1227: 1247), (1228: 1248), (1229: 1248), (1230: 1251), (1231: 1251), (1232: 1254), (1233: 1254), (1234: 1254), (1235: 1256), (1236: 1256), (1237: 1259), (1238: 1259), (1239: 1259), (1240: 1261), (1241: 1262), (1242: 1262), (1243: 1263), (1244: 1266), (1245: 1266), (1246: 1266), (1247: 1267), (1248: 1269), (1249: 1269), (1250: 1271), (1251: 1272), (1252: 1272), (1253: 1274), (1254: 1275), (1255: 1275), (1256: 1277), (1257: 1277), (1258: 1278), (1259: 1278), (1260: 1279), (1261: 1282), (1262: 1282), (1263: 1285), (1264: 1285), (1265: 1286), (1266: 1288), (1267: 1289), (1268: 1289), (1269: 1290), (1270: 1290), (1271: 1290), (1272: 1292), (1273: 1294), (1274: 1294), (1275: 1296), (1276: 1296), (1277: 1297), (1278: 1299), (1279: 1300), (1280: 1301), (1281: 1301), (1282: 1301), (1283: 1303), (1284: 1303), (1285: 1305), (1286: 1305), (1287: 1309), (1288: 1310), (1289: 1310), (1290: 1310), (1291: 1311), (1292: 1312), (1293: 1312), (1294: 1314), (1295: 1316), (1296: 1316), (1297: 1316), (1298: 1319), (1299: 1320), (1300: 1320), (1301: 1320), (1302: 1323), (1303: 1324), (1304: 1326), (1305: 1326), (1306: 1327), (1307: 1327), (1308: 1329), (1309: 1330), (1310: 1330), (1311: 1331), (1312: 1333), (1313: 1335), (1314: 1335), (1315: 1336), (1316: 1336), (1317: 1338), (1318: 1339), (1319: 1339), (1320: 1340), (1321: 1343), (1322: 1344), (1323: 1344), (1324: 1344), (1325: 1346), (1326: 1347), (1327: 1347), (1328: 1348), (1329: 1350), (1330: 1350), (1331: 1352), (1332: 1352), (1333: 1354), (1334: 1354), (1335: 1356), (1336: 1356), (1337: 1358), (1338: 1359), (1339: 1360), (1340: 1360), (1341: 1362), (1342: 1362), (1343: 1364), (1344: 1364), (1345: 1365), (1346: 1366), (1347: 1368), (1348: 1369), (1349: 1369), (1350: 1371), (1351: 1371), (1352: 1373), (1353: 1373), (1354: 1374), (1355: 1376), (1356: 1377), (1357: 1377), (1358: 1379), (1359: 1379), (1360: 1379), (1361: 1382), (1362: 1382), (1363: 1383), (1364: 1384), (1365: 1385), (1366: 1387), (1367: 1388), (1368: 1388), (1369: 1389), (1370: 1391), (1371: 1391), (1372: 1392), (1373: 1394), (1374: 1394), (1375: 1395), (1376: 1396), (1377: 1397), (1378: 1398), (1379: 1399), (1380: 1401), (1381: 1401), (1382: 1401), (1383: 1403), (1384: 1403), (1385: 1406), (1386: 1409), (1387: 1409), (1388: 1409), (1389: 1410), (1390: 1411), (1391: 1411), (1392: 1412), (1393: 1413), (1394: 1415), (1395: 1415), (1396: 1416), (1397: 1417), (1398: 1418), (1399: 1418), (1400: 1421), (1401: 1421), (1402: 1421), (1403: 1423), (1404: 1426), (1405: 1426), (1406: 1426), (1407: 1428), (1408: 1428), (1409: 1428), (1410: 1430), (1411: 1430), (1412: 1431), (1413: 1433), (1414: 1434), (1415: 1434), (1416: 1435), (1417: 1437), (1418: 1437), (1419: 1441), (1420: 1441), (1421: 1441), (1422: 1441), (1423: 1443), (1424: 1444), (1425: 1447), (1426: 1447), (1427: 1447), (1428: 1447), (1429: 1448), (1430: 1450), (1431: 1451), (1432: 1451), (1433: 1453), (1434: 1453), (1435: 1454), (1436: 1457), (1437: 1458), (1438: 1458), (1439: 1459), (1440: 1459), (1441: 1462), (1442: 1463), (1443: 1463), (1444: 1464), (1445: 1464), (1446: 1467), (1447: 1469), (1448: 1470), (1449: 1470), (1450: 1472), (1451: 1472), (1452: 1473), (1453: 1476), (1454: 1476), (1455: 1476), (1456: 1476), (1457: 1477), (1458: 1478), (1459: 1478), (1460: 1479), (1461: 1480), (1462: 1482), (1463: 1482), (1464: 1482), (1465: 1484), (1466: 1485), (1467: 1486), (1468: 1488), (1469: 1488), (1470: 1491), (1471: 1491), (1472: 1491), (1473: 1493), (1474: 1495), (1475: 1495), (1476: 1497), (1477: 1497), (1478: 1498), (1479: 1498), (1480: 1501), (1481: 1502), (1482: 1502), (1483: 1503), (1484: 1505), (1485: 1506), (1486: 1506), (1487: 1508), (1488: 1508), (1489: 1510), (1490: 1512), (1491: 1512), (1492: 1513), (1493: 1513), (1494: 1513), (1495: 1516), (1496: 1516), (1497: 1518), (1498: 1519), (1499: 1519), (1500: 1519), (1501: 1520), (1502: 1522), (1503: 1524), (1504: 1524), (1505: 1525), (1506: 1527), (1507: 1527), (1508: 1529), (1509: 1529), (1510: 1529), (1511: 1531), (1512: 1531), (1513: 1533), (1514: 1534), (1515: 1535), (1516: 1536), (1517: 1537), (1518: 1538), (1519: 1539), (1520: 1541), (1521: 1542), (1522: 1545), (1523: 1545), (1524: 1545), (1525: 1546), (1526: 1546), (1527: 1548), (1528: 1549), (1529: 1549), (1530: 1551), (1531: 1552), (1532: 1552), (1533: 1553), (1534: 1555), (1535: 1555), (1536: 1556), (1537: 1557), (1538: 1559), (1539: 1560), (1540: 1560), (1541: 1562), (1542: 1562), (1543: 1563), (1544: 1565), (1545: 1566), (1546: 1566), (1547: 1568), (1548: 1568), (1549: 1569), (1550: 1572), (1551: 1572), (1552: 1573), (1553: 1573), (1554: 1573), (1555: 1575), (1556: 1576), (1557: 1578), (1558: 1578), (1559: 1579), (1560: 1580), (1561: 1582), (1562: 1583), (1563: 1583), (1564: 1583), (1565: 1585), (1566: 1586), (1567: 1587), (1568: 1587), (1569: 1589), (1570: 1590), (1571: 1591), (1572: 1591), (1573: 1593), (1574: 1593), (1575: 1594), (1576: 1596), (1577: 1598), (1578: 1598), (1579: 1600), (1580: 1600), (1581: 1600), (1582: 1601), (1583: 1603), (1584: 1606), (1585: 1606), (1586: 1606), (1587: 1608), (1588: 1608), (1589: 1609), (1590: 1610), (1591: 1610), (1592: 1611), (1593: 1612), (1594: 1614), (1595: 1614), (1596: 1616), (1597: 1617), (1598: 1617), (1599: 1621), (1600: 1621), (1601: 1623), (1602: 1623), (1603: 1623), (1604: 1624), (1605: 1626), (1606: 1626), (1607: 1626), (1608: 1627), (1609: 1629), (1610: 1630), (1611: 1632), (1612: 1632), (1613: 1633), (1614: 1633), (1615: 1635), (1616: 1637), (1617: 1638), (1618: 1639), (1619: 1639), (1620: 1641), (1621: 1642), (1622: 1642), (1623: 1645), (1624: 1646), (1625: 1646), (1626: 1646), (1627: 1646), (1628: 1647), (1629: 1649), (1630: 1649), (1631: 1649), (1632: 1651), (1633: 1653), (1634: 1655), (1635: 1655), (1636: 1655), (1637: 1659), (1638: 1659), (1639: 1660), (1640: 1660), (1641: 1662), (1642: 1662), (1643: 1663), (1644: 1664), (1645: 1665), (1646: 1666), (1647: 1667), (1648: 1667), (1649: 1669), (1650: 1669), (1651: 1672), (1652: 1672), (1653: 1675), (1654: 1675), (1655: 1675), (1656: 1677), (1657: 1678), (1658: 1678), (1659: 1678), (1660: 1680), (1661: 1680), (1662: 1681), (1663: 1683), (1664: 1685), (1665: 1685), (1666: 1685), (1667: 1686), (1668: 1687), (1669: 1688), (1670: 1690), (1671: 1691), (1672: 1693), (1673: 1693), (1674: 1693), (1675: 1695), (1676: 1696), (1677: 1699), (1678: 1699), (1679: 1700), (1680: 1701), (1681: 1702), (1682: 1702), (1683: 1705), (1684: 1705), (1685: 1705), (1686: 1705), (1687: 1707), (1688: 1707), (1689: 1709), (1690: 1709), (1691: 1712), (1692: 1712), (1693: 1712), (1694: 1714), (1695: 1716), (1696: 1716), (1697: 1717), (1698: 1717), (1699: 1718), (1700: 1721), (1701: 1721), (1702: 1721), (1703: 1723), (1704: 1724), (1705: 1724), (1706: 1725), (1707: 1727), (1708: 1728), (1709: 1729), (1710: 1730), (1711: 1730), (1712: 1732), (1713: 1733), (1714: 1735), (1715: 1735), (1716: 1736), (1717: 1736), (1718: 1737), (1719: 1740), (1720: 1740), (1721: 1740), (1722: 1743), (1723: 1743), (1724: 1744), (1725: 1745), (1726: 1746), (1727: 1746), (1728: 1749), (1729: 1749), (1730: 1750), (1731: 1751), (1732: 1752), (1733: 1752), (1734: 1755), (1735: 1755), (1736: 1755), (1737: 1756), (1738: 1759), (1739: 1759), (1740: 1759), (1741: 1761), (1742: 1762), (1743: 1762), (1744: 1764), (1745: 1764), (1746: 1766), (1747: 1767), (1748: 1768), (1749: 1768), (1750: 1770), (1751: 1771), (1752: 1771), (1753: 1773), (1754: 1773), (1755: 1774), (1756: 1775), (1757: 1776), (1758: 1777), (1759: 1778), (1760: 1779), (1761: 1781), (1762: 1781), (1763: 1783), (1764: 1783), (1765: 1784), (1766: 1786), (1767: 1786), (1768: 1786), (1769: 1788), (1770: 1790), (1771: 1790), (1772: 1790), (1773: 1792), (1774: 1793), (1775: 1794), (1776: 1796), (1777: 1796), (1778: 1800), (1779: 1800), (1780: 1800), (1781: 1800), (1782: 1801), (1783: 1803), (1784: 1804), (1785: 1804), (1786: 1807), (1787: 1808), (1788: 1808), (1789: 1809), (1790: 1809), (1791: 1812), (1792: 1813), (1793: 1813), (1794: 1813), (1795: 1815), (1796: 1815), (1797: 1816), (1798: 1816), (1799: 1817), (1800: 1819), (1801: 1819), (1802: 1820), (1803: 1821), (1804: 1823), (1805: 1823), (1806: 1824), (1807: 1827), (1808: 1827), (1809: 1828), (1810: 1829), (1811: 1830), (1812: 1830), (1813: 1831), (1814: 1834), (1815: 1836), (1816: 1837), (1817: 1837), (1818: 1839), (1819: 1839), (1820: 1839), (1821: 1840), (1822: 1841), (1823: 1842), (1824: 1843), (1825: 1843), (1826: 1845), (1827: 1847), (1828: 1848), (1829: 1848), (1830: 1848), (1831: 1849), (1832: 1851), (1833: 1853), (1834: 1853), (1835: 1853), (1836: 1855), (1837: 1855), (1838: 1856), (1839: 1858), (1840: 1859), (1841: 1859), (1842: 1861), (1843: 1861), (1844: 1864), (1845: 1864), (1846: 1864), (1847: 1866), (1848: 1867), (1849: 1867), (1850: 1869), (1851: 1870), (1852: 1871), (1853: 1872), (1854: 1872), (1855: 1874), (1856: 1877), (1857: 1877), (1858: 1877), (1859: 1878), (1860: 1878), (1861: 1881), (1862: 1882), (1863: 1882), (1864: 1883), (1865: 1885), (1866: 1885), (1867: 1887), (1868: 1887), (1869: 1887), (1870: 1889), (1871: 1892), (1872: 1892), (1873: 1892), (1874: 1893), (1875: 1895), (1876: 1895), (1877: 1896), (1878: 1897), (1879: 1898), (1880: 1900), (1881: 1900), (1882: 1900), (1883: 1900), (1884: 1902), (1885: 1905), (1886: 1905), (1887: 1905), (1888: 1906), (1889: 1908), (1890: 1908), (1891: 1910), (1892: 1910), (1893: 1911), (1894: 1913), (1895: 1914), (1896: 1915), (1897: 1915), (1898: 1917), (1899: 1918), (1900: 1919), (1901: 1919), (1902: 1919), (1903: 1921), (1904: 1922), (1905: 1922), (1906: 1926), (1907: 1926), (1908: 1927), (1909: 1927), (1910: 1928), (1911: 1929), (1912: 1931), (1913: 1931), (1914: 1933), (1915: 1934), (1916: 1935), (1917: 1935), (1918: 1935), (1919: 1937), (1920: 1937), (1921: 1940), (1922: 1941), (1923: 1941), (1924: 1941), (1925: 1945), (1926: 1946), (1927: 1946), (1928: 1946), (1929: 1948), (1930: 1948), (1931: 1948), (1932: 1949), (1933: 1952), (1934: 1953), (1935: 1955), (1936: 1955), (1937: 1956), (1938: 1956), (1939: 1958), (1940: 1958), (1941: 1959), (1942: 1959), (1943: 1961), (1944: 1961), (1945: 1963), (1946: 1963), (1947: 1965), (1948: 1965), (1949: 1966), (1950: 1966), (1951: 1968), (1952: 1968), (1953: 1971), (1954: 1971), (1955: 1972), (1956: 1972), (1957: 1974), (1958: 1974), (1959: 1975), (1960: 1976), (1961: 1977), (1962: 1978), (1963: 1980), (1964: 1980), (1965: 1981), (1966: 1981), (1967: 1983), (1968: 1983), (1969: 1985), (1970: 1985), (1971: 1986), (1972: 1986), (1973: 1988), (1974: 1988), (1975: 1989), (1976: 1989), (1977: 1990), (1978: 1991), (1979: 1992), (1980: 1992), (1981: 1993), (1982: 1994), (1983: 1995), (1984: 1995), (1985: 1996), (1986: 1997), (1987: 1997), (1988: 1998), (1989: 1998), (1990: 1999), (1991: 1999), (1992: 2000), (1993: 2000), (1994: 2000), (1995: 2000), (1996: 2000), (1997: 2000), (1998: 2000), (1999: 2001)"
# top_down = "(0: 1), (1: 3), (2: 4), (3: 5), (4: 7), (5: 8), (6: 9), (7: 10), (8: 12), (9: 13), (10: 14), (11: 15), (12: 16), (13: 18), (14: 19), (15: 20), (16: 21), (17: 22), (18: 23), (19: 24), (20: 26), (21: 27), (22: 28), (23: 29), (24: 30), (25: 31), (26: 32), (27: 33), (28: 35), (29: 36), (30: 37), (31: 38), (32: 39), (33: 40), (34: 41), (35: 42), (36: 43), (37: 44), (38: 45), (39: 47), (40: 48), (41: 49), (42: 50), (43: 51), (44: 52), (45: 53), (46: 54), (47: 55), (48: 56), (49: 57), (50: 58), (51: 60), (52: 61), (53: 62), (54: 63), (55: 64), (56: 65), (57: 66), (58: 67), (59: 68), (60: 69), (61: 70), (62: 71), (63: 72), (64: 73), (65: 75), (66: 76), (67: 77), (68: 78), (69: 79), (70: 80), (71: 81), (72: 82), (73: 83), (74: 84), (75: 85), (76: 86), (77: 87), (78: 88), (79: 89), (80: 90), (81: 92), (82: 93), (83: 94), (84: 95), (85: 96), (86: 97), (87: 98), (88: 99), (89: 100), (90: 101), (91: 102), (92: 103), (93: 104), (94: 105), (95: 106), (96: 107), (97: 108), (98: 109), (99: 110), (100: 112), (101: 113), (102: 114), (103: 115), (104: 116), (105: 117), (106: 118), (107: 119), (108: 120), (109: 121), (110: 122), (111: 123), (112: 124), (113: 125), (114: 126), (115: 127), (116: 128), (117: 129), (118: 130), (119: 131), (120: 132), (121: 133), (122: 135), (123: 136), (124: 137), (125: 138), (126: 139), (127: 140), (128: 141), (129: 142), (130: 143), (131: 144), (132: 145), (133: 146), (134: 147), (135: 148), (136: 149), (137: 150), (138: 151), (139: 152), (140: 153), (141: 154), (142: 155), (143: 156), (144: 157), (145: 158), (146: 159), (147: 161), (148: 162), (149: 163), (150: 164), (151: 165), (152: 166), (153: 167), (154: 168), (155: 169), (156: 170), (157: 171), (158: 172), (159: 173), (160: 174), (161: 175), (162: 176), (163: 177), (164: 178), (165: 179), (166: 180), (167: 181), (168: 182), (169: 183), (170: 184), (171: 185), (172: 186), (173: 187), (174: 188), (175: 189), (176: 190), (177: 192), (178: 193), (179: 194), (180: 195), (181: 196), (182: 197), (183: 198), (184: 199), (185: 200), (186: 201), (187: 202), (188: 203), (189: 204), (190: 205), (191: 206), (192: 207), (193: 208), (194: 209), (195: 210), (196: 211), (197: 212), (198: 213), (199: 214), (200: 215), (201: 216), (202: 217), (203: 218), (204: 219), (205: 220), (206: 221), (207: 222), (208: 223), (209: 224), (210: 225), (211: 226), (212: 227), (213: 228), (214: 230), (215: 231), (216: 232), (217: 233), (218: 234), (219: 235), (220: 236), (221: 237), (222: 238), (223: 239), (224: 240), (225: 241), (226: 242), (227: 243), (228: 244), (229: 245), (230: 246), (231: 247), (232: 248), (233: 249), (234: 250), (235: 251), (236: 252), (237: 253), (238: 254), (239: 255), (240: 256), (241: 257), (242: 258), (243: 259), (244: 260), (245: 261), (246: 262), (247: 263), (248: 264), (249: 265), (250: 266), (251: 267), (252: 268), (253: 269), (254: 270), (255: 271), (256: 272), (257: 273), (258: 274), (259: 275), (260: 276), (261: 277), (262: 278), (263: 279), (264: 280), (265: 281), (266: 282), (267: 284), (268: 285), (269: 286), (270: 287), (271: 288), (272: 289), (273: 290), (274: 291), (275: 292), (276: 293), (277: 294), (278: 295), (279: 296), (280: 297), (281: 298), (282: 299), (283: 300), (284: 301), (285: 302), (286: 303), (287: 304), (288: 305), (289: 306), (290: 307), (291: 308), (292: 309), (293: 310), (294: 311), (295: 312), (296: 313), (297: 314), (298: 315), (299: 316), (300: 317), (301: 318), (302: 319), (303: 320), (304: 321), (305: 322), (306: 323), (307: 324), (308: 325), (309: 326), (310: 327), (311: 328), (312: 329), (313: 330), (314: 331), (315: 332), (316: 333), (317: 334), (318: 335), (319: 336), (320: 337), (321: 338), (322: 339), (323: 340), (324: 341), (325: 342), (326: 343), (327: 344), (328: 345), (329: 346), (330: 347), (331: 348), (332: 349), (333: 350), (334: 351), (335: 352), (336: 353), (337: 354), (338: 355), (339: 356), (340: 357), (341: 358), (342: 359), (343: 360), (344: 361), (345: 362), (346: 363), (347: 364), (348: 365), (349: 366), (350: 367), (351: 368), (352: 369), (353: 370), (354: 371), (355: 372), (356: 373), (357: 374), (358: 375), (359: 376), (360: 377), (361: 378), (362: 379), (363: 380), (364: 381), (365: 382), (366: 383), (367: 384), (368: 385), (369: 386), (370: 387), (371: 388), (372: 389), (373: 390), (374: 391), (375: 392), (376: 393), (377: 394), (378: 395), (379: 396), (380: 397), (381: 398), (382: 399), (383: 400), (384: 401), (385: 402), (386: 403), (387: 404), (388: 405), (389: 405), (390: 407), (391: 407), (392: 409), (393: 409), (394: 411), (395: 411), (396: 412), (397: 413), (398: 414), (399: 415), (400: 416), (401: 417), (402: 418), (403: 419), (404: 420), (405: 421), (406: 422), (407: 423), (408: 424), (409: 425), (410: 426), (411: 427), (412: 428), (413: 429), (414: 430), (415: 431), (416: 432), (417: 433), (418: 434), (419: 435), (420: 436), (421: 437), (422: 438), (423: 439), (424: 440), (425: 440), (426: 441), (427: 442), (428: 443), (429: 444), (430: 445), (431: 446), (432: 447), (433: 448), (434: 449), (435: 450), (436: 451), (437: 452), (438: 453), (439: 454), (440: 455), (441: 456), (442: 457), (443: 458), (444: 458), (445: 459), (446: 460), (447: 461), (448: 462), (449: 463), (450: 464), (451: 465), (452: 466), (453: 467), (454: 468), (455: 469), (456: 470), (457: 470), (458: 471), (459: 472), (460: 473), (461: 474), (462: 475), (463: 476), (464: 477), (465: 478), (466: 479), (467: 479), (468: 480), (469: 481), (470: 482), (471: 483), (472: 484), (473: 485), (474: 485), (475: 486), (476: 487), (477: 488), (478: 489), (479: 490), (480: 490), (481: 491), (482: 492), (483: 493), (484: 494), (485: 494), (486: 495), (487: 496), (488: 496), (489: 497), (490: 498), (491: 498), (492: 499), (493: 499), (494: 500), (495: 500), (496: 500), (497: 500), (498: 500), (499: 501)"
strategy = eval('{'+down_top.replace('(', '').replace(')', '')+'}')
# strategy2 = eval('{'+top_down.replace('(', '').replace(')', '')+'}')
# print([(k, v, strategy2[k]) for (k, v) in strategy.items() if v != strategy2[k]])
# strategy = {0: 1, 1: 2, 2: 4, 3: 5, 4: 7, 5: 8, 6: 9, 7: 10, 8: 12, 9: 13, 10: 14, 11: 15, 12: 16, 13: 18, 14: 19, 15: 20, 16: 21, 17: 22, 18: 23, 19: 24, 20: 26, 21: 27, 22: 28, 23: 29, 24: 30, 25: 31, 26: 32, 27: 33, 28: 35, 29: 36, 30: 37, 31: 38, 32: 39, 33: 40, 34: 41, 35: 42, 36: 43, 37: 44, 38: 45, 39: 47, 40: 48, 41: 49, 42: 50, 43: 51, 44: 52, 45: 53, 46: 54, 47: 55, 48: 56, 49: 57, 50: 58}
strategy = strategy.items()
x, y = zip(*strategy)

plt.scatter(x, y)
plt.show()