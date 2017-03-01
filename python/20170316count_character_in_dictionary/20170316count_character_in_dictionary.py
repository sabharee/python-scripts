string=raw_input("enter the string value:")
dictionary={}
for cha in string:
  if cha not in dictionary:
     dictionary[cha]=1
  else:
     dictionary[cha]=dictionary[cha]+1 
print dictionary
