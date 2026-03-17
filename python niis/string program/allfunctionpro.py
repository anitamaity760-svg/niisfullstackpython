# wap take a string from keyboard count no of character,no of alphabet,nu of upper,nu of lower,no of vowel,no of counconant,no of digit,no of space,no of special symbol,no of word.
print("enter a string")
s=input()
c,alp,up,lw,vw,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
	c=c+1
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up=up+1
		else:
		    lw=lw+1
		if i in"aeiouAEIOU":
		    vw=vw+1
		else:
		    co=co+1
	elif i.isdigit():
	    dg=dg+1
	elif i.isspace():
	    sp=sp+1
	else:
	    sy=sy+1
wd=wd+1
print("no of char=",c)
print("no of alp=",alp)
print("no of up=",up)
print("no of lw=",lw)
print("no of vw=",vw)
print("no of co=",co)
print("no of digit=",dg)
print("no of space=",sp)
print("no of sy=",sy)
print("no of word=",wd)








