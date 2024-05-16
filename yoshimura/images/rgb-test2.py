import cv2
import matplotlib.pyplot as plt 

#画像の読み込み
img = cv2.imread(r"C:\Users\KuratomoOyo\Desktop\yoshimura\images\IMG_8394.jpg")
#BGRからRGBに変換（これしないと画像が変な色になります）
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#plt.imshow(img_rgb)
#print(img_rgb.shape)
print(img_rgb[0:100,0:100,:])