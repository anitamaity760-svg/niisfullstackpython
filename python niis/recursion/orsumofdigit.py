# sum of digit.
def sum_of_digits(n):
	#base case:when n is reduced to a single digit
	if n == 0:
		return 0
	else:
	    #recursive case: last digit+sum of remaining digits
	    return (n%10)+sum_of_digits(n//10)
	# test the function
	number =int(input("enter a number:"))
print(f"the sum of the digits of{125}is:{sum_of_digits(125)}")	

