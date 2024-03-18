import numpy as np

a = np.array([[1,2,30,4],[50,20,30,40]])
print(a.sort())
b = np.array([[5,6,7,4],[1,2,3,4]])
d = np.concatenate([a,b],axis=0)
c = np.concatenate([a,b])
print(d)
print(c)
print(len(c))
print(c.size)



ab = [1,2,3,4,67,6,7,8,10]
largest = 0

print(ab)


a = [1, 2, 3, 4, 67, 6, 7, 8, 10, 90, 3, 2, 3, 1, 1, 2, 2, 2, 2]

# Sort the list for easier counting
a.sort()
print(a)
# Initialize variables
current_element = None
current_count = 0

# Loop through the sorted list and count frequencies
for element in a:
    if element != current_element:
        if current_element is not None:
            print(f"{current_element} occurs {current_count} times")
        current_element = element
        current_count = 1
    else:
        current_count += 1
#
# Print the frequency of the last element
if current_element is not None:
    print(f"{current_element} occurs {current_count} times")



a = 'namanw'
b = a[::-1]
if a ==b:
    print('palindrome')
else:
    print('None')