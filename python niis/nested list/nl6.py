# input from keyboard. 
L=[]
print("enter 2d list data")
L=eval(input())
print("elements are")		
for i in range(0,len(L),1):
    for j in range(0,len(L[i]),1):
        print(L[i][j],end="\t")
    print()
