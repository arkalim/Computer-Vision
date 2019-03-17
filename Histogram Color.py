import cv2
from matplotlib import pyplot as plt

#Read the image
img = cv2.imread(r"C:\Users\arkha\OneDrive\Desktop\photome_threeways.jpg",1)

#Color Format
color = ('b','g','r')

#Plot the histograms for each color channel
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)

plt.show()