# constructor and destructor.
class Demo:
	def __init__(self):
	    print("constructor")
	def __del__(self):
	    print("destructor")
d=Demo()
print("hi")
