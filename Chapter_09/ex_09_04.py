print("Exercise 9.04")

# file is mbox-short.txt



fname = input("Enter file name: ")
fh = open(fname)
lst = list()

committer = dict()

for line in fh:
    if line.startswith('From '):
        pieces = line.split()
        email = pieces[1]
        committer[email] = committer.get(email, 0) + 1
#        count = count + 1
#        print(email)
    else: continue

# print(committer)
bigemail = None
bigcount = None
for email, count in committer.items():
    if bigemail is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
