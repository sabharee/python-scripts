f = open("sample_for_file.txt")
for line in f:
    line = line.rstrip()
    if line.find("i add it") == -1:
        continue
    print line
