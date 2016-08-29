import os
os.chdir("/Users/dancardella/coursera_data_science")
fh = open("Secondaries_Sample_List.csv")
lst = list()
for line in fh:
    line = line.rstrip()
    split_line = line.split()
for word in split_line:
	if not word in lst:
   		lst.append(word)
lst.sort()
print lst
