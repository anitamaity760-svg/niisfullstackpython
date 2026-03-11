class Dog:
	def __init__(self,name,breed,color):
		self.name=name
		self.breed=breed
		self.color=color
	def bark(self):
	    print(self.name,"is barking...")
	def eat(self):
	    print(self.name,"is eating food...")
dog1=Dog("Tommy","Golden Retriver","White")
dog2=Dog("Rocky","German Shepherd","Brown")
dog1.bark()
dog1.eat()
dog2.bark()

