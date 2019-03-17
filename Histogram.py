import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read the image
img = cv2.imread(r"C:\Users\arkha\OneDrive\Desktop\photome_threeways.jpg",1)


color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)

plt.show()

#Stack the histograms side-by-side
#res = np.hstack((b_hist,g_hist,r_hist)) 

#Display the image
#cv2.imshow("Histogram",b_hist)