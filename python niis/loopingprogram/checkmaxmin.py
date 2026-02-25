9.# check max and min no.
print("enter two number")
a=int(input())
b=int(input())
print("1.find maximum")
print("2.find minimum")
choice=int(input("enter your choice:"))
match choice:
  case 1:
   	 print("maximum=",max(a,b))
  case 2:
   	 print("minimum=",min(a,b))
  case _:
    print("invalid choice")   	 