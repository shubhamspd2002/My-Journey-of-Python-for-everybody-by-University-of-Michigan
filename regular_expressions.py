import re
x = 'my 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

import re
x = 'my 2 favourite numbers are nine and six'
y = re.findall('[0-9]*',x) #this gives op at '' because * repeats character o or more times
print(y)

import re
x = 'my twO favourite numbers are nine and six'
y = re.findall('[AEIOU]+',x)
print(y)