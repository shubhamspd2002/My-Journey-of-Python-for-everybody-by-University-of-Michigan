word = 'banana'   #try Banana, ban, bananaaa, bnan, This program is to compare the words in lexicographically, but according to the ASCII code
#so abnan will be before banana and Banana will be after.

if word == 'banana':
    print('all right')

if word < 'banana':
    print('your word ' + word + ', comes before banana')    
elif word > 'banana':
    print('your word ' + word + ', comes after banana')    
else:
    print('all right bananas')  