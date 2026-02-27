 # factorial program in statement 3.
def facttest():
   print("enter a number")
   no=int(input())
   f=1
   for i in range(1,no+1):
     f=f*i
   return f    
result=facttest()   
print("factorial is:",result)