str=raw_input("enter the string value:")
import string
var = string.digits

def function(var,str):
 for element in str:  
  if element in var:
    return -1
    
z=function(var,str)
if z==-1:
  print "string value has digits"
else:
  print "string value has no digits"


