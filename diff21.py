# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

n = int(input())
if(n <= 21):
	print(21-n)
else:
	print(2*(n-21))
