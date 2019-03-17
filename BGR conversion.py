import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

image = img.imread(r"C:\Users\arkha\OneDrive\Desktop\ML\Learning\Data\lena.jpg")


red_component = image[:,:,0]             #separating out red component
green_component = image[:,:,1]             #separating out green component
blue_component = image[:,:,2]             #separating out blue component

BGR = np.array([blue_component,green_component,red_component])
BGR = np.swapaxes(BGR,0,1)
BGR = np.swapaxes(BGR,1,2)

plt.subplot(2,2,1)
plt.title("red component")
plt.imshow(red_component,cmap= 'jet')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.subplot(2,2,2)
plt.title("green component")
plt.imshow(green_component,cmap = 'jet')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.subplot(2,2,3)
plt.title("blue component")
plt.imshow(blue_component,cmap = 'jet')
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.subplot(2,2,4)
plt.title("BGR")
plt.imshow(BGR)
plt.colorbar(orientation = 'horizontal')    #show the colorbar
plt.axis('off')

plt.show()
