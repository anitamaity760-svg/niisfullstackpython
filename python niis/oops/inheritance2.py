class person:
	def display__persion(self):
	    print("This is a person")
class student(person):
    def display__student(self):
        print("This is a student")
class engineering(student):
    def display__engineering(self):
        print("This is an engineering student")
e=engineering()
e.display__persion()
e.display__student()
e.display__engineering()                	    	

 		