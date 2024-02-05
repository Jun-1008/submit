import xml.etree.ElementTree as ET 
import csv
import numpy as np
import cv2


list_XY = []
heightmap_array = []

i = 0
j = 0
k = 2
# for k in range(300):
with open ('./xml2hm2/b5_hm2.csv', 'w', newline='') as f0: #書き込み用csv
    writer = csv.writer(f0)

    with open ('pixel_xml.csv', 'r') as f00: #提供したデータ y,x,X,Y
        line00 = csv.reader(f00)
        for row00 in line00:
            # print(row00[2:4])
            # ['207', '-144']['207', '-144'] X,Y部分の抽出成功
            # list_XY.append(row00) #まだh無し
    # print(list_XY)
    # [, , ['44', '224', '207', '-144']]

            tree = ET.parse('./xml_backmap/build/5.scape') # XMLファイルオープン
            root = tree.getroot()

            for i in range(317):
                count = root[4][i][2].text #これで0番目のcountを取得　2
                # h = root[5][int(count)-1][1].text #i番目のボクセルのMAX高さ　5　この場合は下に1つボクセル情報ある
                # 今回の都市は浮いていないのでcountをそのまま使えばOK
                # h= の式が何かがおかしい、正確な値を拾えていない
                XML_X = root[4][i][0].text
                XML_Y = root[4][i][1].text
                # print(count, h, XML_X, XML_Y)
                # 1 0 9 -72 OK

                if row00[2:4] == [XML_X, XML_Y]:
                    heightmap_array = [row00[1], row00[0], count] #pixelのx, y, h こうしないとハイトマップの向きがおかしい
                    writer.writerow(heightmap_array)
                    # print(heightmap_array)
                    # print(heightmap_array)
                    # ['196', '25', '0']
                    # ['205', '30', '0']
                    # print(row00[0:2])
                    # ['196', '25']
                    # ['205', '30']

img = np.zeros((256, 256))
with open('./xml2hm2/b5_hm2.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # get x, y, z
        x = int(row[1])
        y = int(row[0])
        z = float(row[2])/14*255
        img[x, y] = z
        # print(x, y, z)


# print(img.shape)
cv2.imwrite('./xml2hm2/b5_hm2.png', img)

