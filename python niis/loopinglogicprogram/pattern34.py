""" 1234321
     12321
      121
       1 """
for i in range(4,0,-1):
    for j in range(4-i,0,-1):
        print(end=" ")
    for j in range(1,i+1,1):
    	print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")	
    print() 	