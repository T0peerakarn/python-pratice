# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front.

text = str(input())
n = int(input())
prefix = ""
ans = ""
for i in range (0, min(3, len(text))):
  prefix += text[i];
for i in range (0, n):
  ans += prefix
print(ans)
