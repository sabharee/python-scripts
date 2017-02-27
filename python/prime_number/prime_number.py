a=2
number=int(raw_input("enter a number:"))
while number > a:
  if number%a==0 and a!=number:
    print "it is not a prime number"
    a=a+1    
  else:
    print "it is a prime number"
    a=number+1
