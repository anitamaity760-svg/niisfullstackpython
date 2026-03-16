# customise exception or user define exception.
class VotterError(BaseException):
	def __init__(self):
		super().__init__()
print("enter age")
age=int(input())
if age>=18:
    print("eligbal")
else:
    raise VotterError("age not allow") 
print("main end")
