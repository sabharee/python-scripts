def iseven(x):
  if x%2==0:
    return True 
  else:
    return False

condn = iseven(14)
if condn:
  print "14 is even"
else:
  print "14 is odd"