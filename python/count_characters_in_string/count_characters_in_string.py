x=raw_input("enter the string:")
y=raw_input("enter the character of string to count:")
def letter(x):
  fruit=x
  count=0    
  for char in fruit:    
    if char == y:
      count = count+1
  print count
letter(x)
