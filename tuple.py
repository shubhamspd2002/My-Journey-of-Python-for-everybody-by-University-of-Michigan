y = 'ABC'
print(y)
print(y[2])

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
    
tups = d.items()
print(tups)

fhand = open('romeo.txt') #this program is to make a histogram of the list of words in the text file
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
lst = list() #this program is to reverse the positions of key, val to val,key
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

last = sorted(lst, reverse=True) #this is to sort the values but in reverse order. only the sorted function without the reverse=True will sort in low to high order

for val, key in lst[:10]: #to print top 10 highest values but in key,val orientation
    print(key, val)    


c = {'a':10, 'b':1, 'c':22} #this is a dictionary
t = (sorted([(v,k) for k,v in c.items()])) #this program is a combination of the above 3 paragraphs from lst to print(key,val). This program tells that for every k,v in c.items , convert it to v,k 
s = sorted(t, reverse=True)#print it from high v to low v
p = t.sort(reverse=True)
print(t, '\n', s)