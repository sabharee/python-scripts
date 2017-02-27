first_number=int(raw_input("enter first number or 0 to stop:"))
smallest_number=first_number
next_number=int(raw_input("enter next number or 0 to stop:"))
while next_number != 0:     
  if next_number < smallest_number:
    smallest_number=next_number
  next_number=int(raw_input("enter next number or 0 to stop:")) 
print smallest_number

