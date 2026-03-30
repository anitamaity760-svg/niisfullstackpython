"""4
   3 4
   2 3 4
   1 2 3 4"""
n=4
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end="\t")
    print() 
          