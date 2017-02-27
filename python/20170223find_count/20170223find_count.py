def letter(str,ch,start):
  fruit=str
  number=start
  count= 0
  while number<len(fruit):
    if fruit[number] == ch:
      count = count+1
    number=number+1
  print count
letter("furniture","r",2)
