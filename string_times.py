# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

a = str(input())
n = int(input())
ans = ""
for i in range (0, n):
	ans += a
print(ans)
