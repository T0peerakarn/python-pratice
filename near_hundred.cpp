# Given an int n, return True if it is within 10 of 100 or 200.

n = int(input())
print(abs(100-n) <= 10 or abs(200-n) <= 10)
