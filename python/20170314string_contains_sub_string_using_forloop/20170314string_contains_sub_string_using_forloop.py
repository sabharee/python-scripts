str=raw_input("enter the string value:")
ch=raw_input("enter the string to find the position:")
def find(str,ch):
  index=0
  if ch in str:
    c=ch[0]
    for cha in str:
      if cha == c:
        if str[index:index+len(ch)]==ch:
           return index
      index=index+1
  return -1     

z=find(str,ch)
print z
