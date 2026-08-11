exp = ["17","4","3","*","1","5","+","/","*"]
stack=[]
for i in exp:
	if i.isdigit():
		stack.append(int(i))
	else:
	    b=stack.pop()
	    a=stack.pop()
	    if i == "+":
	        stack.append(a+b)
	    elif i == "-":
	        stack.append(a-b)
	    elif i == "*":
	        stack.append(a*b)  
	    elif i == "/":
	        stack.append(a/b)
print("final result =",stack.pop())	                  	