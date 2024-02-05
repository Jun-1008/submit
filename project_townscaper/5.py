import csv
import numpy as np
import itertools
import xml.etree.ElementTree as ET
import xml.dom.minidom

csv_num = 44 #解析対象のファイル番号、又したの2箇所も変更。またcsv->xml dirでformatから同じ番号の追記ファイルを用意
xml_list = []
list0 = []
list1 = []
list_XY = []

# with open (str(csv_num) + 'x.csv', 'r') as f0: #対象ファイルはxmlの X, Y, h
with open ('oldx.csv', 'r') as f0: #対象ファイルはxmlの X, Y, h

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
height = 0 #enumerate関数結果。cornerの代表値のh。直後に+1
h_num = 0 #V追加時にfor文で入れる

# やるべきはリアルなhを含む情報を持つxml_listが幾つあるかを数えたい

for i, j in enumerate(list_XY): #0 ['9', '-72']  1 ['9', '-63'] ... 316 ['207', '-144']
    for h in range(14):
        # list_sample.append([j[0], j[1], str(h)]) # print  [['9', '-72', '0'], ['9', '-72', '1'], ... ,['207', '-144', '13']]
        frequency = xml_list.count([j[0], j[1], str(h)])
        # print(frequency) #1, 1, 0, ..., 1
        list_fre.append(frequency) #そのXYのh0~13がどれだけあるか、リストに数値が入っている
    height = [index_num for index_num, max_fre in enumerate(list_fre) if max_fre == max(list_fre)]
    height = max(height) + 1 #max_freが2つ以上同数で被っていた場合、ここで大きい方のインデックスを採用
    if height == 14:
        height = 1
    # このheightがそのcorner座標で最も頻度が高かったh

    tree = ET.parse("C:\\Users\\picco\\OneDrive\\デスクトップ\\TS_data\\44.scape") #空ファイル
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
    tree.write("C:\\Users\\picco\\OneDrive\\デスクトップ\\TS_data\\44.scape") #空ファイル
    
    h = 0 #そのcornerの高さ情報
    frequency = 0 #頻度を代入
    list_fre = [] #frequencyをappendするリスト
    index_num = 0 #enumerate関数内のみ。リストの中の最大のhのインデックス＝h はどこか
    max_fre = 0 #enumerate関数内のみ。最大頻度数
    height = 0 #enumerate関数結果。cornerの代表値のh。直後に+1
    h_num = 0 #V追加時にfor文で入れる
    
    