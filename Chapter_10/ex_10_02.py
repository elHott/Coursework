print("Exercise 10.02")

# file is mbox-short.txt

fname = input("Enter file name: ")
# if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)

committer = dict()

for line in fh:
    if line.startswith('From '):
        pieces = line.split()
        time = pieces[5]
        tpieces = time.split(':')
        hour = tpieces[0]
        committer[hour] = committer.get(hour, 0) + 1
    else: continue

for k,v in sorted(committer.items()):
    print(k,v)

'''
bigemail = None
bigcount = None
for email, count in committer.items():
    if bigemail is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
'''
