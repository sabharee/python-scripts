str=int(raw_input("enter the total number of strings in list:"))
a=[]
index=0
while index<str:
   next_str=raw_input("enter the string value")
   a.append(next_str)
   index=index+1

def func(a):
  iterm=0                                
  count=0
  back=-1                      
  for big in a:
    while count<len(big):    
      if big[count]==big[back]:                   
        back=back-1
        count=count+1
        iterm=iterm+1
      elif iterm != len(big):
        print big, " is not a palindrome"
        break
      else:
        pass  
    if iterm == len(big): 
       print big," is a palindrome"
                          
func(a)           
                       
