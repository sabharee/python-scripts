
def addition(x,y):
  z=x+y
  print z

def subtraction(x,y):
  z=x-y
  print z

def multiplication(x,y):
  z=x*y
  print z

def division(x,y):
  z=x/y
  print z
x=int(raw_input("enter first number:"))
y=int(raw_input("enter next number:"))
e=raw_input("enter_operation_to_perform")
if e=="+":
   addition(x,y)
elif e=="-":
   subtraction(x,y)
elif e=="*":
   multiplication(x,y)
elif e=="/":
   division(x,y)
else:
   pass
