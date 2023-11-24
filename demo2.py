import matplotlib.pyplot as plt
import numpy as np
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(3, 1, 1)
plt.plot(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(3, 1, 2)
plt.plot(x,y,marker='o',ms=20,mfc='b')

#plot 3:
x = np.array([10, 20, 25, 30])
y = np.array([20, 40, 60, 40])
plt.subplot(3, 1, 3)
plt.plot(x,y,marker='+',ms=20)


plt.show()