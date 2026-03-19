# inserting multiple value in list.
L=[10,20,30,40,50]
L[1:1:1]=[15,17,18]
print(L)


# inserting multiple value in list using range().
L=[10,20,30,40,50]
L[1:1:1]=range(5)
print(L)

L=[10,20,30,40,50]
L[1:1:1]="hi"
print(L)

L=[10,20,30,40,50]
L[5:5:1]="hi"
print(L)



