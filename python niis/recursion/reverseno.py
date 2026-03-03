# reverse no.
def reverse_number(n,rev=0):
	#base case:when n becomes 0,return the reversed number
	if n == 0:
		return rev
	else:
	    #recursive case:shift current rev by 1 digit and add the last digit of n
	    return reverse_number(n//10,rev*10+n%10)
	# test the function
	number =int(input("enter a number:"))
reversed_num=revers_number(number)
print(f"the reverse of {number}is:{reversed_num}")	

