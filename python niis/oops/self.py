class Student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
    def show(self):
    	print(id(self))
    	print("my name=",self.name)
    	print("my rollno=",self.roll)
    	print("my mark=",self.mark)
s=Student("mitu",1,90.50)
print(id(s))
s.show()
