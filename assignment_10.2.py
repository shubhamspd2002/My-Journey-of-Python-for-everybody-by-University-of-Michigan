#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.     

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dicc = dict()
for line in handle:
    if line.startswith('From '):
        a = line.split()
        b = a[5]
        hour = b.split(':')
        hr = hour[0]
        dicc[hr]=dicc.get(hr,0)+1
        
for k,v in sorted(dicc.items()): #sorted can be used with variable.items() to arrange them in alphabetical order
    print(k,v)
    