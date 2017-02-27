n=int(raw_input("enter the total number of list value"))
a=[]
index=0
while index<n:
  b=raw_input("enter the value")
  a.append(b)  
  index=index+1   
for r in a:
  z=len(r)
  print "length of",r,"is",z     


