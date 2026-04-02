"""1
   3 2
   4 5 6
   10 9 8 7"""
num=1
for i in range(1,5,1):
	row=list(range(num,num+i))
	num+=i
	if i%2==0:
	   row=row[::-1]     
	print(*row)          