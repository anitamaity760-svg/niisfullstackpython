# simple interest program 2.
class simple:
	def __init__(self,principal,rate,time):
	    self.principal=principal
	    self.rate=rate
	    self.time=time
	def show(self):
	    print("principal=",self.principal)
	    print("rate=",self.rate)
	    print("time=",self.time)
	def sical(self):
	    return self.principal*self.rate*self.time/100
print("enter principal rate and time")
#i1=simple(float(input()),float(input()),float(input()))
pr=float(input())
r=float(input())
t=float(input())
i1=simple(pr,r,t)
i1.show()
print("simple interest=",i1.sical())


