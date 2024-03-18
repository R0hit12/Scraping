import numpy as np

a = np.array([[1,2,3,4],[2,3,2,4],[3,2,3,4]])
b = np.array([[10,20,30,40],[100,200,300,400]])

c = np.array([[1,2,3,4],[5,6,7,8]])

d = np.array([2])
print(np.add(b,c))

c = np.power(c,d)
print(c)

c = (np.sqrt(c))
print(c)

c = c.astype(int)
print(c)


# print(np.subtract(a,b))

