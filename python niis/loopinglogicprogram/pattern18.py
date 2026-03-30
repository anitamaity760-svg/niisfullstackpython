"""D C B A
   D C B
   D C 
   D   """ 
    
for i in range(4,0,-1):
    for j in range(i):
        print(chr(68-j),end="\t")
    print()       