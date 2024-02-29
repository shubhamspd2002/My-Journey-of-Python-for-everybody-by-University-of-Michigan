# download the data: http://py4e-data.dr-chuck.net/regex_sum_1917936.txt (There are 101 values and the sum ends with 30). hange file name to 
# something not starting with t, r and n because when path file is copied, it inccorporates "\t" a tab, "\n"  newline, and "\r" carriage return.
#In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters
 

import re

fname = input("Enter file name: ")  #here directly enter the file path. You can find the file path by right clicking on the txt file and copy as path.
fname = fname.replace('"', '')
fh = open(fname)

lst = list()

for lines in fh:
    line = lines.rstrip()
    main = re.findall('[0-9]+', line)
    for nums in main:
        nums = float(nums)
        lst.append(nums)
    
print(sum(lst))    