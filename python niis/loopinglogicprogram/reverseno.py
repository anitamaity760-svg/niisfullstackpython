# wap initialize no 125 reverse no.
no=125
s=0
while no!=0:
	r=no%10
	s=s*10+r
	no=no//10
print("rev no=",s)	