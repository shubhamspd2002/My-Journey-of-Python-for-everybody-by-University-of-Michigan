#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of 
# the person who sent the message). 
# Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to
# see how to print the count.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
fname = fname.replace('"', '')
fh = open(fname)
count = 0

for line in fh:
    splt = line.rstrip().split()
    if line.startswith('From '): #here if you put 'From' then the data repeats twice. Find out the reason
        count += 1
        print(splt[1])
    
        


print("There were", count, "lines in the file with From as the first word")

#or u can do like this: 


han = input('enter file name: ')
han = han.replace('"', '')
han = open(han)
coount = 0
for line in han:
    line = line.rstrip()
    wds = line.split()
    
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[1])
    coount += 1
    
print("There were", coount, "lines in the file with From as the first word")