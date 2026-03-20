# input from keyboard. no 1 way 2D list data.
L=[]
print("enter how many list store")
s=int(input())
for i in range (0,s,1):
	print("enter list1 data")
	x=eval(input())
	L.append(x)
print("elements are")
for i in range(0,len(L),1):
    for j in range(0,len(L),1):
        print(L[i][j],end="\t")
    print()
