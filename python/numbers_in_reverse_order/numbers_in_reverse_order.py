n=int(raw_input("Enter the last Number to stop:"))
def numbers(n):
  if n != 0:
    print n
    numbers(n-1)
  else:
    print n
    
numbers(n)
