di = {'car':3, 'bike':2, 'auto':7, 'cycle':5}
tpl = (di.items()) #tpl is now a tuple
print('tpl: ',tpl)
print('Sorted tpl: ',sorted(tpl)) #this will sort according to the 1st element of the tuple
tmp = list()

print('tmp line by line: ')
for k,v in di.items():
    print(k,v)
    newt = (v,k)
    tmp.append(newt)
    
print('Flipped: ',tmp)

tmp = sorted(tmp) #this now will sort according to the ascending order of the 2nd element of the tuple (we flipped it earlier)

print('Sorted: ',tmp)

rev_tmp = sorted(tmp, reverse=True)
print('Reverse of tmp: ',rev_tmp)

print('Sorted rev_tmp 1st 2 tuples: ',rev_tmp[:2])

print('flipped back to normal :')
for v,k in rev_tmp[:2]: 
    print(k,v)

#so through all of these program we were able to print according to the
#ascending value of the 2nd part of tuple and keeping it at the 2nd position