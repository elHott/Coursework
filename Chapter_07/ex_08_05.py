print("Exercise 8.05")

# file is mbox-short.txt



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count = 0

for line in fh:
    if line.startswith('From '):
        pieces = line.split()
        email = pieces[1]
        count = count + 1
        print(email)
    else: continue

print("There were", count, "lines in the file with From as the first word")
