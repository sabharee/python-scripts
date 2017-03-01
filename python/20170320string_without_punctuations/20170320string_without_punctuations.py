punctuations='''~`!@#$%^&*()_+-=[]\{}|;':",./<>?'''
str=raw_input("enter the string value:")
no_punctuation=""
for cha in str:
  if cha not in punctuations:

    no_punctuation=no_punctuation+cha
  else:
    pass
print no_punctuation
