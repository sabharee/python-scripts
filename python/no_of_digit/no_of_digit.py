def finding_the_digit(n):
   
   dividend=n
   no_of_remainder=0
   q=dividend/10
   r=dividend%10
   no_of_remainder=no_of_remainder+1
   while q!=0:
    dividend=q
    q=dividend/10
    r=dividend/10
    no_of_remainder=no_of_remainder+1 
   no_of_digit=no_of_remainder
   
   print no_of_digit
finding_the_digit(2017)
