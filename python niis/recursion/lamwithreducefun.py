#lambda with reduce().
from functools import reduce
numbers=[1,2,3,4]
result=reduce(lambda a,b:a+b,numbers)
print(result)