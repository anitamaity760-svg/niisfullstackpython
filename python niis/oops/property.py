class Student:
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
	    self.__name=value
s=Student("mitu")
print(s.name)
s.name="anita"
print(s.name)
	    	
		
