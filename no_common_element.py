# Write a Python program to check if two given sets have no elements in common
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8}
s3 = {9, 10, 11}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s2.isdisjoint(s3))  # return True if none of item present in both sets otherwise False
 
