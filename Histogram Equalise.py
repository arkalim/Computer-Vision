import cv2
import numpy as np

#Read the image
img = cv2.imread(r"C:\Users\arkha\OneDrive\Desktop\photome_threeways.jpg",1)

#Split the color channels
b,g,r = cv2.split(img)

#Equalise each color channel
b_equ = cv2.equalizeHist(b)
g_equ = cv2.equalizeHist(g)
r_equ = cv2.equalizeHist(r)

#Merge the color channels
equ = cv2.merge((b_equ,g_equ,r_equ))

#Stack the images side-by-side
res = np.hstack((img,equ)) 

#Display the image
cv2.imshow(r"C:\Users\arkha\OneDrive\Desktop\photome_res.jpg",res)