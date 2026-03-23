# set comprehensive.
s={5,8,9,12,8}
s1={i for i in s}
print(s1)

# 2.
s={5,8,9,12,8}
s1={i for i in s if i>8}
print(s1)

# 3.
s="welcome"
s={i for i in s if i in "aeiou"}
print(s)
