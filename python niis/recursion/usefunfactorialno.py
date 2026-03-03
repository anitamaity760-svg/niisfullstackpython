#use function factorial no.
def fact(no):
    f=1
    while no>0:
       f=f*no
       no=no-1
    return f 
res=fact(4)
print("factorial=",res)
