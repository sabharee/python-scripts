total_number=int(raw_input("enter the total number:"))
index=0
a=[]
while index < total_number:
  number=int(raw_input("enter the number"))
  a.append(number)
  index=index+1

for r in a:
    z=r%2  
    print r
 
    if z==0:       
      print  "is a even number"
    else:
      print  "is a odd number"    
