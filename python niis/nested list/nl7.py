# matrix addition.
L1=[[1,2,3],[4,5,6]]
L2=[[3,4,1],[2,2,4]]
L3=[[0,0,0],[0,0,0]]
for i in range (0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		L3[i][j]=L1[i][j]+L2[i][j]
print(L3)


# substraction.
L1=[[1,2,3],[4,5,6]]
L2=[[3,4,1],[2,2,4]]
L3=[[0,0,0],[0,0,0]]
for i in range (0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		L3[i][j]=L1[i][j]-L2[i][j]
print(L3)

# matrix multiplication.
L1=[[1,2,3],[4,5,6]]
L2=[[3,4,1],[2,2,4]]
L3=[[0,0,0],[0,0,0]]
for i in range (0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		L3[i][j]=L1[i][j]*L2[i][j]
print(L3)						