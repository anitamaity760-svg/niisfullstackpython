# transpose matrix.
L1=[[1,2,3],[4,5,6]]
L2=[[0,0],[0,0],[0,0]]
for i in range (0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		L2[j][i]=L1[i][j]
print(L2)