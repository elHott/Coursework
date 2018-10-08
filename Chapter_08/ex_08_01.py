print("Exercise 8.01")

# file is romeo.txt

# go back and rewatch chapter 8

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst: lst.append(word)
lst.sort()
print(lst)
