import re
a=raw_input("enter the mail id:")
if re.match(r'sabari', a):
    if re.search(r'gmail.com', a):
        print a

