#6 setdefault().
d={1:"A",2:"B",4:"C",3:"C"}
print(d.setdefault(1))


d={1:"A",2:"B",4:"C",3:"C"}
print(d.setdefault(5))
print(d)


d={1:"A",2:"B",4:"C",3:"C"}
print(d.setdefault(6,"F"))
print(d)