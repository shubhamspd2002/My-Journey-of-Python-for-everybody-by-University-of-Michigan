#http://www.py4e.com/code3/romeo.txt download the text file and save

print('enter a file path: ') 
file = input('')

#if len(file) < 1 : file = (enter file path) This line is to make a default file run, in case u just press enter while putting file name 

file = file.replace('"', '')
hand = open(file)

di = dict()
for line in hand:
    wds = line.rstrip().split()
    for w in wds:
        print(w)
        if w in di:
            di[w] = di[w]+1
            print('***EXITSTING***')
        else:
            di[w] = 1
            print('**New**')
        print(di[w])

print(di)        
    
#or you can use this instead of if and else
'''
si = dict()
for line in hand:
    wds = line.rstrip().split()
    for w in wds:
        oldcount = si.get(w,0) #this get functn sees whether there is a value for a word w. If yes, then it moves ahead, if no then its a new word and it is assigned the value 0 to w 
        print(w,'old',oldcount)
        newcount = oldcount+1
        si[w] = newcount
        print(w,'new',newcount)

print(si)
'''
#or the simpler way

'''
fi = dict()
for line in hand:
    wds = line.rstrip().split()
    for w in wds:
        fi[w] = fi.get(w,0)+1
        print(w,'new',fi[w])

print(fi)

'''
#following is to print the most occuring w

largest = -1
theword = None #n always capital
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k #to remember the word



print('Done: ', theword, largest)