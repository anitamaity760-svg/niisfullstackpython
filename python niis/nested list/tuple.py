# tuple sequency format.
t=10,"hi",2.5
for i in t:
	print(i)

# use range().
t=(10,"hi",2.5)
for i in range(len(t)):
    print(t[i])

   
# predefine funtion in tuple.
t=(10,"hi",2.5,10,"bye")
print(t.count(10))
print(t.index(2.5))
