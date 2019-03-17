import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

image = img.imread(r"C:\Users\arkha\OneDrive\Desktop\ML\Learning\Data\lena.jpg")


red_component = image[:,:,0]             #separating out red component
green_component = image[:,:,1]             #separating out green component
blue_component = image[:,:,2]             #separating out blue component

plt.subplot(1,3,1)
plt.title("red component")
red_img_plot = plt.imshow(red_component,cmap= 'gray')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.subplot(1,3,2)
plt.title("green component")
green_img_plot = plt.imshow(green_component,cmap = 'gray')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.subplot(1,3,3)
plt.title("blue component")
blue_img_plot = plt.imshow(blue_component,cmap = 'gray')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.show()
