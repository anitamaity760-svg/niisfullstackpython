# sum of digit recursion.
s=0
def sdtest(no):
  global s
  if no!=0:
    s=s+no%10
    no=no//10
    sdtest(no)
  return s
res=sdtest(125) 
print("sumof digit=",res) 	