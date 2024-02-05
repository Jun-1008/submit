import xml.etree.ElementTree as ET 
import csv

list_XY = []    
heightmap_array = []
h1 = []
i = 0 #足場の数だけ

tree = ET.parse('10.scape') # XMLファイルオープン。これは学習データの大元
root = tree.getroot()

with open ('10all.csv', 'w', newline='') as f0: #書き込み用csv
    writer = csv.writer(f0)

    with open ('pixel_xml.csv', 'r') as f00: #提供したデータ y,x,X,Y
        line00 = csv.reader(f00)
        for row00 in line00:

            for i in range(594): # 足場が594個
                count = root[4][i][2].text # このroot1は学習データ
                #これで0番目のcountを取得
                # 学習データの/count数は594個
                # if count == '11':    
                XML_X = root[4][i][0].text
                XML_Y = root[4][i][1].text

                if row00[2:4] == [XML_X, XML_Y]:
                    heightmap_array = [row00[1], row00[0], count] #pixelのx, y, h こうしないとハイトマップの向きがおかしい
                    writer.writerow(heightmap_array)
                    # print(heightmap_array)
                    print(XML_X, XML_Y)
                    # ['196', '25', '0']
            # ['205', '30', '0']
                # print(row00[0:2])
                # ['196', '25']
                # ['205', '30']

