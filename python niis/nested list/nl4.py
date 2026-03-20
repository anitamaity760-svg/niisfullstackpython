# input from keyboard. no 1 way 2D list data.in other way
L=[]
print("enter how many list store")
s=int(input())
for i in range (0,s,1):
	x=[]
	print("enter list",i+1,"how many data")
	s1=int(input())
	for j in range(0,s1,1):
		print("enter element",j+1)
		x.append(int(input()))
	L.append(x)
print("elements are")		
for i in range(0,len(L),1):
    for j in range(0,len(L),1):
        print(L[i][j],end="\t")
    print()
