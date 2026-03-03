#  use resursion print 10to1 no.
def show(i):
	if i<10:
	   show(i+1)
	print(i)   
def main():	
    show(1)	
main()    
