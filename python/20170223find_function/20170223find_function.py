def find(str,ch):
  index = 0
  while index<len(str):
    if str[index] == ch:
      return index
    index=index+1
  return -1

position = find("furniture","r") 
print "position of the element is",position
