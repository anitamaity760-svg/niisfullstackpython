#1. display indivisual letter line by line.
s="welcome"
for i in range(0,7,1):
	print(s[i])
# 2.
s="welcome ram"
for i in range(0,11,1):
	print(s[i])
#3.
s="welcome"
for i in range(0,len(s),1):
	print(s[i])
#4.
s="welcome"
for i in range(-len(s),0,1):
	print(s[i])	
# display string backword every indivisual letter.
s="welcome"
for i in range(len(s)-1,-1,-1):
	print(s[i])	
# display string backword every indivisual letter.
s="welcome"
for i in range(-1,-len(s)-1,-1):
	print(s[i])		