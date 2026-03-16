# parent class 
class persion:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show_persion(self):
	    print("Name :",self.name)
	    print("Age :",self.age)
#child class
class student(persion):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
    def show_student(self):
        print("Roll No :",self.roll)
#grand child class
class enggstudent(student):
    def __init__(self,name,age,roll,branch):
         super().__init__(name,age,roll)
         self.branch=branch
    def show_engg(self):
        print("Branch :",self.branch) 
#object creation
e=enggstudent("Mitu",20,101,"computer science")
#calling method
e.show_persion()
e.show_student()
e.show_engg()                        	    	  