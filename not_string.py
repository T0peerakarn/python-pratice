# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged

a = str(input())
if(a[0:3] == "not"):
	print(a)
else:
	print("not " + a)
