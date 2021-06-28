# Given a non-empty string and an int n,
# return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).


a = str(input())
n = int(input())
ans = ""
for i in range (0, n):
	ans += a[i]
for i in range (n+1, len(a)):
	ans += a[i]
print(ans)
