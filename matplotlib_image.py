import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

image = img.imread(r"C:\Users\arkha\OneDrive\Desktop\ML\Learning\Data\lena.jpg")
#print(image)

red_component = image[:,:,0]             #separating out red component
red_img_plot = plt.imshow(red_component,cmap = 'jet')
plt.colorbar()    #show the colorbar
plt.axis('off')
plt.show()
