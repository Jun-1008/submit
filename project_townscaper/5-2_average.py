import csv
# import numpy as np
import itertools
import xml.etree.ElementTree as ET
import xml.dom.minidom

csv_num = 7 #解析対象のファイル番号、また下の2箇所も変更。またcsv->xml dirでformatから同じ番号の追記ファイルを用意
xml_list = []
list0 = []
list1 = []
list_XY = []

# with open ('.\\model2_SUS\\csv_data\\' + str(csv_num) + 'x.csv', 'r') as f0: #対象ファイルはxmlの X, Y, h
with open ('.\\raw_data\\b5x.csv', 'r') as f0: #対象ファイルはxmlの X, Y, h

    line0 = csv.reader(f0, delimiter=",")
    for row0 in line0:
        xml_list.append(row0) #コレで解析対象ファイルの[X, Y, h]が全てリストになった

with open ('used_XY.csv', 'r') as f1: # X,Y
    line1 = csv.reader(f1)
    for row1 in line1:
        list_XY.append(row1) #まだh無し
# [['9', '-72'], ['9', '-63'], ['18', '-99'], , ['207', '-144']]
#print(list_XY[0]) ['9', '-72']

h = 0 #そのcornerの高さ情報
frequency = 0 #頻度を代入
list_fre = [] #frequencyをappendするリスト
index_num = 0 #enumerate関数内のみ。リストの中の最大のhのインデックス＝h はどこか
max_fre = 0 #enumerate関数内のみ。最大頻度数
frequency_num = 0
height = 0 #enumerate関数結果。cornerの代表値のh。直後に+1
h_num = 0 #V追加時にfor文で入れる
total_floor = 0
total_frequency = 0
average = 0

# やるべきはリアルなhを含む情報を持つxml_listが幾つあるかを数えたい

for i, j in enumerate(list_XY): #0 ['9', '-72']  1 ['9', '-63'] ... 316 ['207', '-144']
                                # このリストはxmlファイルの座標を上から順にとったリスト
    for h in range(14):
        # list_sample.append([j[0], j[1], str(h)]) # print  [['9', '-72', '0'], ['9', '-72', '1'], ... ,['207', '-144', '13']]
        frequency = xml_list.count([j[0], j[1], str(h)])
        # スケッチ後に変換したシンハイトマップに対し、1つのxml座標の0~13のhが幾つあるか頻度を調べる
        # print(frequency) #1, 1, 0, ..., 1
        list_fre.append(frequency) #そのXYのh0~13がどれだけあるか、リスト[]に数値が入っている
        # つまりインデックスが階情報に相当。ただし、0のcountは1（足場のみ）、13はcount14相当で14階
    # height = [index_num for index_num, max_fre in enumerate(list_fre) if max_fre == max(list_fre)]
    for index_num, frequency_num in enumerate(list_fre):
        total_floor += index_num * frequency_num
        total_frequency += frequency_num
    if total_frequency == 0:
        height = 1
    else:
        average = total_floor / total_frequency
        height = int(average) + 1 
    # +1はcount数に合わせる（count 0だとデータにならない）ために足している。

    # tree = ET.parse(".\\model2_SUS\\" + str(csv_num) + ".scape") #空ファイル
    tree = ET.parse(".\\xml_backmap\\" + "5" + ".scape") #空ファイル
    root = tree.getroot()
    for corners in root.findall('corners'):
        s_c = ET.SubElement(corners, 'C')
        s_x = ET.SubElement(s_c, 'x')
        s_y = ET.SubElement(s_c, 'y')
        s_count = ET.SubElement(s_c, 'count')
        s_x.text = j[0] #x.
        s_y.text = j[1] #y.
        s_count.text = str(height)
        
    for voxels in root.findall('voxels'):
        for h_num in range(height):
            s_v = ET.SubElement(voxels, 'V')
            s_t = ET.SubElement(s_v, 't')
            s_h = ET.SubElement(s_v, 'h')
            if h_num == 0:
                s_t.text = '15'
            else:
                s_t.text = '14'
            s_h.text = str(h_num)

    tree = ET.ElementTree(root)
    # tree.write("C:\\Users\\picco\\OneDrive\\デスクトップ\\TS_data\\44.scape") #空ファイル
    tree.write(".\\xml_backmap\\" + "5" + ".scape") #空ファイル
    
    h = 0 #そのcornerの高さ情報
    frequency = 0 #頻度を代入
    list_fre = [] #frequencyをappendするリスト
    index_num = 0 #enumerate関数内のみ。リストの中の最大のhのインデックス＝h はどこか
    max_fre = 0 #enumerate関数内のみ。最大頻度数
    height = 0 #enumerate関数結果。cornerの代表値のh。直後に+1
    h_num = 0 #V追加時にfor文で入れる
    frequency_num = 0
    total_floor = 0
    total_frequency = 0
    average = 0
    
    