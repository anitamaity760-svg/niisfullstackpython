"""A
   B A
   C B A
   D C B A"""
n=4
for i in range(n):
    for j in range(i,-1,-1):
        print(chr(65+j),end="\t")
    print() 
          