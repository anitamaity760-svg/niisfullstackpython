# using constructor and parameter.
class Demo:
	def __show(self):
	    print("hi")
	def disp(self):
	    self.__show()
ob=Demo()
# ob.__show() error
ob.disp()
