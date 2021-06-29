# Given a string, return the count of the number of times
# that a substring length 2 appears in the string and also
# as the last 2 chars of the string, so "hixxxhi" yields 1
# (we won't count the end substring).

text = str(input())
n = int(len(text))
pattern = text[n-2:]
ans = int(0)

for i in range (0, n-2):
	if(pattern == text[i:i+2]):
		ans += 1

print(ans)
