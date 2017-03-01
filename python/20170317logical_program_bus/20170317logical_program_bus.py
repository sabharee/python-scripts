#based on the input decide whether there is sufficient busses or not and 
#give solution for how many extra busses required.

bus=int(raw_input("enter the total number of buses:"))
seat=int(raw_input("enter the total number of seats in a bus:"))
people=int(raw_input("enter the total number of people to travel:"))

total=bus*seat
index=1

if total < people:
  a=people - total
  while a>seat:
    a=a-seat
    index=index+1
  print index," extra buses required"
elif total>=people:
  print "no extra buses required"
else:
  pass
