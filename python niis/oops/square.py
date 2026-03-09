# square program.
class square:
	def __init__(self,num):
		self.num=num
	def find_square(self):
	    result=self.num*self.num
	    print("square is:",result)
# object create
n=int(input("enter a number:"))
obj=square(n)
# method call
obj.find_square()	
    	