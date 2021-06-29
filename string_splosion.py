# Given a non-empty string like "Code" return a string like "CCoCodCode".

text = str(input())
ans = ""
  
for i in range (0, len(text)):
	for j in range (0, i+1):
		ans += text[j]
   
print(ans)
