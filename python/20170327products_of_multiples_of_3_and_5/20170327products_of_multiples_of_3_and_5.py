number = int(raw_input("enter total numbers of natural number:"))
list = []
while number > 0:
    list.append(number)
    number = number - 1
print "numbers in list are:",list
z = []
for a in list:
    b = a % 3
    c = a % 5
    if b == 0 or c == 0:
        z.append(a)
    else:
        pass
print "natural numbers division of 3 and 5 in lists are:", z
p=reduce(lambda x, y: x*y, z)
print "multiple of natural numbers are", p
