""" D 
    C D
    B C D
    A B C D"""
n=4
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(64+j),end="\t")
    print()
            