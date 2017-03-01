str=int(raw_input("enter the total number of strings in list:"))
a=[]
index=0
while index<str:
   next_str=raw_input("enter the string value")
   a.append(next_str)
   index=index+1
z=set(a)
print z
