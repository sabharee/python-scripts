print "Enter 2 numbers"
first_number=int(raw_input("enter first number:"))
second_number=int(raw_input("enter next number:"))
x=raw_input("enter_operation_to_perform")
if x=="+":
   a=first_number + second_number
   print a
elif x=="-":
   a=first_number - second_number
   print a
elif x=="*":
   a=first_number * second_number
   print a
elif x=="/":   
   a=float(first_number) / second_number    
   print a
else:
   pass
