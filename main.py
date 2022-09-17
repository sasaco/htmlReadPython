from a import read_a
from b import read_b
from c import read_c
from d import read_d
from e import read_e
import csv
import os
import glob


file_Path = 'Z:/二重矢板/result'
csv_Path = 'Z:/二重矢板/csv'
error_files = glob.glob("Z:/error/*")
error_numbers =  [os.path.splitext(os.path.basename(file))[0] for file in error_files ]

result_list = [['No',
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6',
    'b1', 'b2', 'b3', 'b4',
    'c1', 'c2', 'c3', 'c4',
    'd1','d2',
    'e1_0', 'e1_1', 'e2_0', 'e2_1', 'e3_0', 'e3_1', 'e4_0', 'e4_1', 
    'e5_0', 'e5_1', 'e6_0', 'e6_1', 'e9_0', 'e9_1', 'e10_0', 'e10_1'
    ]]

Minimum = 1
Maximum = 100000

for i in range(Minimum, Maximum + 1):
    try:
        if str(i) in error_numbers:
            continue   # エラーフォルダに番号があったらスキップ

        # a 
        file_a = os.path.join(file_Path, '{}a.html'.format(i)) 
        if not os.path.isfile(file_a):
            continue # フォルダにファイルがなかったらスキップ

        a1, a2, a3, a4, a5, a6 = read_a(file_a)

        # b
        file_b = os.path.join(file_Path, '{}b.html'.format(i)) 
        if not os.path.isfile(file_b):
            continue # フォルダにファイルがなかったらスキップ
        
        b1, b2, b3, b4 = read_b(file_b)

        # c
        file_c = os.path.join(file_Path, '{}c.html'.format(i)) 
        if not os.path.isfile(file_c):
            continue # フォルダにファイルがなかったらスキップ

        c1, c2, c3, c4  = read_c(file_c)

        # d
        file_d = os.path.join(file_Path, '{}d.html'.format(i)) 
        if not os.path.isfile(file_d):
            continue # フォルダにファイルがなかったらスキップ

        d1, d2 = read_d(file_d)

        # e
        file_e = os.path.join(file_Path, '{}e.html'.format(i)) 
        if not os.path.isfile(file_e):
            continue # フォルダにファイルがなかったらスキップ
        e1_0, e1_1, e2_0, e2_1, e3_0, e3_1, e4_0, e4_1, e5_0, e5_1, \
        e6_0, e6_1, e9_0, e9_1, e10_0, e10_1 = read_e(file_e)

        # 集計した結果をリストに収集
        result_list.append([i,
        a1, a2, a3, a4, a5, a6,
        b1, b2, b3, b4,
        c1, c2, c3, c4,
        d1, d2,
        e1_0, e1_1, e2_0, e2_1, e3_0, e3_1, e4_0, e4_1, e5_0, e5_1,
        e6_0, e6_1, e9_0, e9_1, e10_0, e10_1
        ])

    except ValueError as e:
        pass

with open("result{}-{}.csv".format(Minimum, Maximum), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(result_list)
