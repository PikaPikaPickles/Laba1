import matplotlib.pyplot as plt
import numpy as np
X = list()
Y = list()
FileName = input()
for i in range(1, int(np.genfromtxt(FileName, delimiter='\t', dtype=str)[0]) + 1):
    X.append(float(np.genfromtxt(FileName, delimiter='\t', dtype=str)[i].split()[0]))
    Y.append(float(np.genfromtxt(FileName, delimiter='\t', dtype=str)[i].split()[1]))
    print(i)
plt.scatter(X, Y)
plt.axis('equal')
plt.ylabel('Our Tochkas')
plt.show()
