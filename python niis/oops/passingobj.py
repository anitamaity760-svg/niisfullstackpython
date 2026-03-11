# wap to passing referance in argument.
class Student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
def show(s):
	    print("my name=",s.name)
	    print("my rollno=",s.roll)
	    print("my mark=",s.mark)
s=Student("mitu",1,90.50)
show(s)
