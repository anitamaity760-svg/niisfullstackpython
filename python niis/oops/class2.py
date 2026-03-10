class Demo:
	#classmethod it call by classname but it call by object
	@classmethod
	def show(cls):
	    print("hi")
Demo.show()
d=Demo()
d.show()

	
