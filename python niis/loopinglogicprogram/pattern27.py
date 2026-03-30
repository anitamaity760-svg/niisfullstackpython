""" A B C D
    B C D
    C D 
    D """
n=4
for i in range(n):
    for j in range(i,n):
        print(chr(65+j),end="\t")
    print() 
           