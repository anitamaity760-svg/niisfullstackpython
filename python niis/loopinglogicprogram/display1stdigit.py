# wap initialize no 125 display 1st digit.
no=125
while no!=0:
	r=no%10
	no=no//10
print("first digit=",r)


# using single variable display 1st digit.
no=-125
if no<=0:
   no=-no
while no>=10:
   no=no//10
print("first digit=",no)       	