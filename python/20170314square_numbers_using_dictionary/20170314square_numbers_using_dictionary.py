total_number=int(raw_input("enter the total number of intergers:"))
a=[]
index=0
while index<total_number:
  numbers=int(raw_input("enter the numbers to perform square in dictionary:"))       
  a.append(numbers)
  index=index+1
b={}
for index in a:   
  b[index]=index**2
print b

