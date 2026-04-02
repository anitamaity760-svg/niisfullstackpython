# find prime no in 10 to 20.
for no in range(10,21,1):
	d=2
	c=0
	while d<=no//2:
		if no%d==0:
			c=c+1
			break
		d=d+1	
	if c==0:
		print(no,"prime no")
	else:
	    print(no,"not prime no")

