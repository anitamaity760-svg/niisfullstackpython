# reverse string.
def reverse_string(s):
    if len(s)==0:
       return s
    return reverse_string(s[1:])+s[0]
name="anita" 
print(reverse_string(name))
