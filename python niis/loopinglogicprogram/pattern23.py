"""D C B A
   C B A
   B A
   A"""
n=4
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(chr(64+j),end="\t")
    print() 
          