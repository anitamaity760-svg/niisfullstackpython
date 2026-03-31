"""4 3 2 1
   4 3 2
   4 3 
   4 """
   
for i in range(1,5,1):
    for j in range(4,i-1,-1):
        print(j,end="\t")
    print()       