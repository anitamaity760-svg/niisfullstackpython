 # factorial program in statement 4.
def facttest(n):
   f=1
   for i in range(1,no+1):
     f=f*i
   return f
print("enter a number:")   
no=int(input())   
result=facttest(no)   
print("factorial of",no,"is",result)