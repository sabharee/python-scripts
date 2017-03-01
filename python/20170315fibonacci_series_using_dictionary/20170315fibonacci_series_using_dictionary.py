previous={0:1,1:1}
n=int(raw_input("enter the total number"))
def fibonacci(n):
  if previous.has_key(n)
     return previous[n]
  else:
     newvalue = fibonacci(n-1) + fibonacci(n-2)
     previous[n] = newvalue
     return newvalue
fibonacci(n)
