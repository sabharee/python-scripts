str=int(raw_input("enter the total number of strings in list:"))
a=[]
index=0
while index<str:
   next_str=raw_input("enter the string value")
   a.append(next_str)
   index=index+1

biggest_number=a[0]
for big in a:
  x=len(big)
  
  if x>len(biggest_number):     
    biggest_number=big

print biggest_number
