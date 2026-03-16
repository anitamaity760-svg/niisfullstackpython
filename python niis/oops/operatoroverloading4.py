class MyTime:
	def __init__(self,h,m,s):
		self.h=h
		self.m=m
		self.s=s
	def __gt__(self,t2):
		if self.h>t2.h:
			return True
		elif self.h==t2.h:
		    if self.m>t2.m:
		        return True
		    elif self.m==t2.m:
		        if self.s>t2.s:
		            return True
		return False
	def show(self):
	    print(self.h,":",self.m,":",self.s)	 
t1=MyTime(5,40,35)
t2=MyTime(5,40,30)
print("Time 1:")
t1.show()
print("Time 2:")
t2.show()
if t1>t2:
   print("t1 is bigger than t2")
else:
   print("t2 is bigger than t1") 

		