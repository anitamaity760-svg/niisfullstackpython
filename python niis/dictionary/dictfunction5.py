# 5 d.fromkeys().
d={1:"A",2:"B",4:"C",3:"F"}
d.fromkeys("welcome")
print(d)


#   example.
d={1:"A",2:"B",4:"C",3:"F"}
d.fromkeys("welcome","ok")
d['e']="bye"
print(d)

#   example.
d1={1:"A",2:"B",4:"C",3:"F"}
d1.fromkeys(range(5))
print(d1)
