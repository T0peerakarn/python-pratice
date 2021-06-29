# Given a string, return a new string made of every even index of the old string

text = str(input())
ans = ""
n = int((len(text) + len(text)%2) / 2)
for i in range (0, n):
	ans += text[i*2]
print(ans)
