# list comprehensive in python.
L=[5,8,6,3,8,7,7,12]
L1=[i for i in L]
print(L1)

# adding 3 in each element.
L=[5,8,6,3,8,7,7,12]
L1=[i+3 for i in L]
print(L1)

# adding 3 in all even no.
L=[5,8,6,3,8,7,7,12]
L1=[i+3 for i in L if i%2==0]
print(L1)
