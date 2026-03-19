# string element stored in list.
s="welcome"
L=[]
for i in s:
	if i not in L:
		L.append(i)
print(L)

# vowel element stored in list.
s="welcome"
L=[]
for i in s:
	if i in "aeiouAEIOU":
		L.append(i)
print(L)

# counconant element stored in list.
s="welcome"
L=[]
for i in s:
	if i not in "aeiouAEIOU":
		L.append(i)
print(L)