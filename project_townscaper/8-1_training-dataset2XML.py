import xml.etree.ElementTree as ET 
import csv

list_XY = []    
heightmap_array = []
h1 = []

with open ('pixel_xml.csv', 'r') as f00: #提供したデータ y,x,X,Y
    line00 = csv.reader(f00)
    for row00 in line00:
        list_XY.append(row00) #まだh無し

i = 0
j = 0
k = 2

tree = ET.parse('trg0.scape') # XMLファイルオープン。これは学習データの大元
root = tree.getroot()
tree2 = ET.parse('trg0_h1.scape') # XMLファイルオープン。書き込み先
root2 = tree2.getroot()


for corners in root2.findall('corners'): # ループせずcornersに追記するだけ
                                        # root2は書き込み先
    for i in range(241): # 足場が241個
        count = root[4][i][2].text # このroot1は学習データ
        #これで0番目のcountを取得
        # 学習データの/count数は241個
        XML_X = root[4][i][0].text
        XML_Y = root[4][i][1].text

        s_c = ET.SubElement(corners, 'C')
        s_x = ET.SubElement(s_c, 'x')
        s_y = ET.SubElement(s_c, 'y')
        s_count = ET.SubElement(s_c, 'count')
        s_x.text = XML_X
        s_y.text = XML_Y
        if count == '5': # 5は例
            s_count.text = count
        else:
            s_count.text = '1'
            count = 1

        for voxels in root2.findall('voxels'):
            for h_num in range(int(count)):
                s_v = ET.SubElement(voxels, 'V')
                s_t = ET.SubElement(s_v, 't')
                s_h = ET.SubElement(s_v, 'h')
                if h_num == 0:
                    s_t.text = '15'
                else:
                    s_t.text = '14'
                s_h.text = str(h_num)

tree2 = ET.ElementTree(root2)
tree2.write("trg0_h1.scape")

