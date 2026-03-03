#sum of digit useing function.
def sdtest(no):
     s=0
   while no!=10:
   	  r=no%10
   	  s=s+r
   	  no=no//10
   return s
print(sdtest(125))   	  