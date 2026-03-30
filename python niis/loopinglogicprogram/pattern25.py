""" 1 2 3 4
    2 3 4
    3 4 
    4"""
n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end="\t")
    print() 
          