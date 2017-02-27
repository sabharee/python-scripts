 =raw_input("enter the string:")

def palindrome(q,element):   
  while q<len(a):
   if a[q]==a[element]:     
     q=q+1
     element=element-1
     y=1+palindrome(q,element)
     return y     
   else:
     return 1   
  return 1 

z=palindrome(0,-1)-1
if z==len(a):    
  print "it is a palindrome"
else:
  print "it is not palindrome" 


     
