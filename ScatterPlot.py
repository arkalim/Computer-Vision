import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]   #x axis 
y = [5,2,4,2,1,4,5,2]   #y axis

plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o") #s is the size of the marker

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()   #not needed
plt.show()
