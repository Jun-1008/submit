import numpy as np
import csv
import os
import cv2

img = np.zeros((256, 256))
    # 256x256の0で初期化された二次元配列を作成

with open('./raw_data/b5.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # get x, y, z
        x = int(row[0])
        y = int(row[1])
        z = float(row[2])/14*255
        img[x, y] = z
        print(x, y, z)


# print(img.shape)
cv2.imwrite('./csv2heightmap/b5.png', img)