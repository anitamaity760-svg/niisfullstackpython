# display the element in matrix from useing sequency().
L=[[10,20,30,],[40,50,60],[70,80,90]]
for i in L:
	for j in i:
		print(j,end="\t")
	print()


# display the element in matrix from useing range().
L=[[10,20,30,],[40,50,60],[70,80,90]]
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()
				