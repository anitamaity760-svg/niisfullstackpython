11.#  1.add 2.sub 3.mult 4.divide.
print("enter two number:")
a=int(input())
b=int(input())
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=int(input("enter your choice:"))
match choice:
   case 1:
     print("addition=",a+b)
   case 2:
     print("subtraction=",a-b)
   case 3: 
     print("multiplication=",a*b)
   case 4: 
     if b!=0:
       print("division=",a/b) 
     else:
       print("cannot divide by zero")
   case _:      
       print("invalid choice")