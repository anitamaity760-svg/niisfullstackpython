from abc import *
class Demo(ABC):
	@abstractmethod
	def show(self):
		pass
class Demo1(Demo):
    def show(self):
        print("hi")
#d=Demo() error
d1=Demo1()
d1.show()

