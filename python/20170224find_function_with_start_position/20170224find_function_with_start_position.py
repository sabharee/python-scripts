def find(str,ch,start):
  index =start
  while index<len(str):
    if str[index] == ch:
      return index    
    index=index+1
  return -1

position = find("sabari","i",2)

if position != -1:
   print "position of the element is",position
else:
   print "character is not available in string"
