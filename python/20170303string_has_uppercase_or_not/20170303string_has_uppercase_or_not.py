str=raw_input("enter the string value")
import string
upper_case=string.uppercase

def function(str,upper_case):
  for val in str:
   if val in upper_case:
     return -1


z=function(str,upper_case)
if z==-1:
  print "string contains uppercase character" 
else:
  print "string has no uppercase character"  
