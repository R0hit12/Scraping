import numpy as np

a = np.array([[1,2,30,4],[50,20,30,40]])
print(a.sort())
b = np.array([[5,6,7,4],[1,2,3,4]])
d = np.concatenate([a,b],axis=0)
c = np.hstack([a,b])
print("==-=-=-=--==",d)

# print(c)
# c.sort()
# print(c)
print(len(d))
print(c.size)



split_ar = np.array([1,2,3,2,4,5,6,7,8,9,10])
a = np.array_split(split_ar,2)
print(a)

print(a[0][0:3])