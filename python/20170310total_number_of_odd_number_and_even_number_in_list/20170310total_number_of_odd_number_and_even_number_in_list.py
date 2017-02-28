total_number=int(raw_input("enter the total number:"))
index=0
a=[]

while index < total_number:
  number=int(raw_input("enter the number"))
  a.append(number)
  index=index+1

def func(a):
  index=0
  count=0
  for r in a:
    z=r%2        
    if z==0:       
      index=index+1      
    else:
      count=count+1
  print "total number of odd numbers in list is", count
  print "total number of even numbers in list is", index
    
func(a)          
