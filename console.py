PyDev console: starting.
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
import numpy as np
A= np.random.rand(2, 2)
B= np.random.rand(2, 2)

#elemental operation in A
np.sum(A[:,1])
np.float64(0.26996550216690884)
np.sum(A[1,:])
np.float64(0.6921918417581141)
np.sum(np.diag(A))
np.float64(0.5445112952522253)

#elemental operations in B
np.sum(B[1, :])
np.float64(0.9060530982693604)
np.sum(B[:, 1])
np.float64(0.5811749531251079)
np.sum(np.diag(B))
np.float64(0.5577222812569236)
A+B
array([[0.40850489, 0.15741177],
       [0.90451625, 0.69372869]])
A*B
array([[0.03127275, 0.00400512],
       [0.20453387, 0.10847467]])

#matrix operation
C=np.dot(A, B)
print(C)
[[0.04564599 0.05300246]
 [0.15355559 0.16546831]]
print(A)
[[0.30645966 0.03191387]
 [0.45414021 0.23805163]]