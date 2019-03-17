import matplotlib.pyplot as plt
import numpy as np

#load the csv file(txt file) and unpack it into x and y 
x, y = np.loadtxt(r"C:\Users\arkha\OneDrive\Desktop\ML\Learning\Data\read_data.txt", delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
