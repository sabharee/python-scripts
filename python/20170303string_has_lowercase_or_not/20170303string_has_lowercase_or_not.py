str=raw_input("enter the string value:")
import string
lower_case=string.lowercase
def function(str,lower_case):
 for val in str:
  if val in lower_case:
    return -1

z=function(str,lower_case)    
if z==-1:
  print "string contains lowercase character"
else:
  print "string has no lowercase character" 
