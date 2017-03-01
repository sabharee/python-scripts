total_number=int(raw_input("enter the total number of intergers:"))
a=[]
index=0
while index<total_number:
  numbers=int(raw_input("enter the numbers:"))       
  a.append(numbers)
  index=index+1
z=set(a)
print z
c=list(z)
print c
