"""4 3 2 1
   4 3 2
   4 3 
   4 """
n=4   
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j,end="\t")
    print()       