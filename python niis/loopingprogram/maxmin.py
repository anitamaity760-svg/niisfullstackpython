10.# check vowel and consonant.
ch=input("enter a character:").lower()
print("1.check vowel")
print("2.check consonant")
choice=int(input("enter your choice:"))
match choice:
  case 1:
    if ch in 'aeiou':
   	 print("vowel")
    else:
   	 print("not a vowel") 	
  case 2:
    if ch.isalpha() and ch not in 'aeiou':
   	 print("consonant")
   	else:
   	 print("not a consonant")
  case _:
    print("invalid choice")   	
