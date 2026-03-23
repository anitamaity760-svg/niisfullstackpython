# remove duplicate element and ordering from.
L=[5,8,7,5,9,6,4,5,8]
d=set(L)
print(d)



L=[5,8,7,5,9,6,4,5,8]
d1={}
d1=d1.fromkeys(L)
print(d1)

L=[5,8,7,5,9,6,4,5,8]
d1={}
d1=d1.fromkeys(L)
L=list(d1.keys())
print(L)
