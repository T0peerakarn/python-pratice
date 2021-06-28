# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.

a = input()
b = a.split()
print(a[0] == "6" or a[len(a)-1] == "6")
