# simple interest program.
class simpleinterest:
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
i1=simpleinterest(1000,10,2)
i1.show()
print("simple interest=",i1.sical())

