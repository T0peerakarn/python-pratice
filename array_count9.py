# Given an array of ints, return the number of 9's in the array.

text = str(input())
text += " "
ans = int(0)
now = ""

for i in text:
	if(i == " "):
		if(now == "9"):
			ans += 1
		now = ""
	else:
		now += str(i);
          
print(ans)
