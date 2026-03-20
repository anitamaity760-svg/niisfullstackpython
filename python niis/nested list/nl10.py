# without list comprehensive in 2D list.
L1=[[1,2,3],[4,5,6]]
L2=[]
for i in L1:
	x=[]
	for j in i:
		x.append(i)
	L2.append(x)
print(L2)

# using list comprehensive.
L1=[[1,2,3],[4,5,6]]
L2=[[j for j in i]for i in L1]
print(L2)
