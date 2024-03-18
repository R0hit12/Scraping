import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.append(a,[7,8,9.3])
print(b)
b = b.astype(int)
print(b)

b = np.insert(b,5,[20,49])
print(b)

s = np.where(b%3==0)
print(s)