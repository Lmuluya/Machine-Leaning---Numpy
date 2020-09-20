# Creating a numpy array
# Using the ndaray objects
import numpy as np
a = np.arange(6).reshape(2,3)
print(a)
# The dimension of array a
print("Dimension of the array"); print(a.ndim)
print("Shape of the array"); print(a.shape)
print("Size of the array");print(a.size)
print("Type of the array"); print(a.dtype)
print("Item size"); print(a.itemsize)

## Attributes of an array
c = np.array(([1,2,3]),dtype=complex)
print(c)
print("Item size"); print(c.itemsize)
print(np.zeros((2,3)))
print(np.zeros((3,3),dtype=np.int16))



