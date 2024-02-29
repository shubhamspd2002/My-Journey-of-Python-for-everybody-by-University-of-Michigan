#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

name = input("Enter file:")
file = open(name)
collectn = dict()
lst = list()

for line in file:
    if line.startswith('From '):
        words = line.split()
        lst.append(words[1])
            
            
for words in lst:
    collectn[words] = collectn.get(words,0) + 1


bestword = None #N must be capital of None or else error will come
count = 0
for key,value in collectn.items():
    if value is None or value > count:
        count = value
        bestword = key


print(bestword, count)