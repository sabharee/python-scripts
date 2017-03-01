f=open("sample_for_file.txt")
for line in f:
    #strip reduce the gap
    line = line.rstrip()
    if line.startswith("i"):
        print line

