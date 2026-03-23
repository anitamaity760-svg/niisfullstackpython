# update the key value.
d={}
d[1]="A"
d[2]="B"
d[1]="C"
print(d)

#1.
d={}
d["B"]="A"
print(d)

#2.
d={}
d[1]=(4,5,6)
print(d)

#3.
d={1:"A",3:"B",2:"C"}
print(d)

#4.
d={1:"A",3:"B",2:"C"}
print(d)
print(d[3])

#5.
d={1:"A",True:"B",3:"C",3:"D"}
print(d)
