
import cv2
import matplotlib.pyplot as plt
#plt.style.use('seaborn')
img = cv2.imread(r"C:\Users\ASUS\Pictures\Saved Pictures\Dragon-Ball-Z-Goku-Super-Saiyan-1000-Wallpaper-9.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.subplot(1,2,2)
plt.imshow(final,cmap="gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.show()
