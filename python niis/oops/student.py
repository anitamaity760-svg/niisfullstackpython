# wap to display 2 student name,rollno,mark.
class student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
    def show(self):
	    print("my name=",self.name)
	    print("my rollno=",self.roll)
	    print("my mark=",self.mark)

s1=student("anita",1,90.50)
s2=student("mitu",2,80.50)	

s1.show() 
s2.show() 
