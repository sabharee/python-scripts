str=raw_input("enter the string value:")
import string
small_letters =string.lowercase
capital_letters =string.uppercase


def function(str,small_letters,capital_letters):
  for element in str:
    if element in small_letters:
       return -1
    elif element in capital_letters:
       return -1

z=function(str,small_letters,capital_letters)
if  z== -1:
   print "string value contains alphabets"
else:
   print "string value has no alphabets" 
