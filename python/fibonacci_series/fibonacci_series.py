n=int(raw_input("enter the fibonacci number:"))
a=0
print a
b=1
print b
count=2
if n<=0:
 print ("print only positive integes")
while count<n:
  z = a + b
  a = b
  b = z
  print z
  count += 1   
  
