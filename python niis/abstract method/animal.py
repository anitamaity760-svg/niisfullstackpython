from abc import *
class Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
class Dog(Animal):
    def sound(self):
        return"Bark"
class Cat(Animal):
    def sound(self):
        return"Meow"
d=Dog()
c=Cat()
print("Dog sound:",d.sound())
print("Cat sound:",c.sound())          			
       				       		