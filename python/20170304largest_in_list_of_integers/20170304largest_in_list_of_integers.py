total_number(raw_input("enter the total number of intergers:"))
a=[]
index=0
while index<total_number:
  numbers=int(raw_input("enter the numbers:"))       
  a.append(numbers)
  index=index+1


largest_number=a[0]
for big in a:

  if big>largest_number:
    largest_number=big

print largest_number
