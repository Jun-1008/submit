import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

input_image = './junk/407.png'

# 画像をグレースケールで読み込む, 0はグレースケール
gray = cv2.imread(input_image, 0)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# 169が採用値。投稿用に150に変更

cv2.imwrite('./junk/407b1.jpg', binary)
plt.imshow(binary, cmap='gray')
plt.show()