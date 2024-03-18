import numpy as np

a = np.array([[1,2,3,4],[2,3,2,4],[3,2,3,4]])
b = np.array([2,3,4])
b = b.astype(float)
print(type(b))
print(b)
print(a)
print(a[1][3])
print(a[1,3])
print(np.shape(a))
print(np.size(a))

print(len(a[1]))