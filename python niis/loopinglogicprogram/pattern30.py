"""12344321
    123321
    1221
    11"""
for i in range(4,0,-1):
    for j in range(1,i+1,1):
        print(j,end="")
    for j in range(i,0,-1):
        print(j,end="")    
    print()       