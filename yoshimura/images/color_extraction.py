import numpy as np
import cv2

#画像の読み込み
img = cv2.imread(r"C:\Users\KuratomoOyo\Desktop\yoshimura\images\IMG_8394.jpg")
#BGRからRGBに変換（これしないと画像が変な色になります）
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#画像のサイズを小さくする（前処理）
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img_rgb,(round(width/4), round(height/4)))

#青を抽出
bgr = [90,150,20]
thresh = 20

#色の閾値
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

#画像の2値化
maskBGR = cv2.inRange(resized_img,minBGR,maxBGR)
#画像のマスク（合成）
resultBGR = cv2.bitwise_and(resized_img, resized_img, mask = maskBGR)

cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result mask", maskBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()