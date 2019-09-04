#Multiplies and adds matrices independently.
import numpy as np

A = np.matrix('6 8; 9 12')
B = np.matrix('7 5; 4 8')
C = A + B
D = A @ B

print(C)
print(D)