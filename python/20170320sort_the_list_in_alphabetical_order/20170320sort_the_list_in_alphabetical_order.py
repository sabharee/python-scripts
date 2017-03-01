total=int(raw_input("enter the total number of list:"))

lis=[]
index=0
while index<total:
    str=raw_input("enter the string value:")  
    lis.append(str)
    index=index+1
lis.sort()
for var in lis:
  print var 
