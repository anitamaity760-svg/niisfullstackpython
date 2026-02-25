12.# find out mark.
marks=int(input("enter your marks(0-100):"))
print("1,check grade")
choice=int(input("enter your choice:"))
match choice:
  case 1:
    match marks:
print("Grade:A")     
     case_if marks>=75:  
print("Grade:B")     
     case_if marks>=60:
print("Grade:C")     
     case_if marks>=40: 
print("Grade:D")     
     case_if marks>=0:  
print("Grade:F")     
     case_:print("invalid marks")     
  case_:
    print("invalid choice")     
