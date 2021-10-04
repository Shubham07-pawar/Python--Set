#  Write a Python program to remove the intersection of a 2nd set from the 1st set.
s1 = {10, 20, 30, 40, 50, 13, 91}
s2 = {10, 20, 30, 40, 55, 11, 12}

s2 -= s1
print(s2.difference(s1))
print(s2)
s3 = {()}
print(type(s3))





