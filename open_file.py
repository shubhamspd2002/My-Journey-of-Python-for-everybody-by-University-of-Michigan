files = open(r"C:\Users\LENOVO\Desktop\hello.txt") #mote that open does not read the file. It just helps us to access it.
count = 0
for cheese in files:
    count += 1
    print(cheese)   
print('line count =', count)   
#read whole file
inp = files.read()
print(len(inp))
print(inp[:10])

print('break\n')

# here It seems like you are trying to read the contents of a file, count the number of lines, and print the first 10 characters. 
# However, there is an issue in above code. Once you iterate over the lines in the file using a for loop, the file pointer
# is at the end of the file, and subsequent attempts to read the file using files.read() will result in an empty string.

file_path = r"C:\Users\LENOVO\Desktop\hello.txt"

# Open the file using a 'with' statement to ensure proper file closure
with open(file_path, 'r') as files:
    count = 0
    for line in files:
        count += 1
        print(line)

    print('line count =', count)

# Reopen the file or use the stored content for further processing
with open(file_path, 'r') as files:
    # Read the whole file
    content = files.read()

print('the length of the lines are: ', len(content)) #the op will be a number but it will be a char
n = 10  
print('here are the first', n ,'lines: ', content[:n], '\n')

#This code uses the with statement to automatically close the file after reading its contents. 
# Additionally, it separates the file reading and counting lines from reading 
# the whole file content. If you need to perform multiple operations on the file, you can reopen 
# it or use the stored content (content variable) as needed.

print('break\n')

with open(file_path, 'r') as files: 
    for line in file_path:  #here there is an issue that as u hv opened file_path as files, u should mention for line in files
        if line.startswith('from'):
            print(line)
            
print('break\n')

file_path = r"C:\Users\LENOVO\Desktop\hello.txt"

# Open the file using a 'with' statement to ensure proper file closure
with open(file_path, 'r') as files:
    for line in files: #this line is to read the lines in files, one line at a time. line here is an iterration variable
        if line.startswith('from'):
            print(line)

print('break\n')
#here there are gaps between new lines because there was an invisible \n present and the print statement adds new \n 
#we can remove this bu strip function

with open(file_path, 'r') as files:
    for line in files:
        line = line.rstrip()
        if line.startswith('from'):
            print(line)
            
print('\nbreak\n')

with open(file_path, 'r') as files:
    for line in files:
        line = line.rstrip()
        if not line.startswith('to'): #this says that if the line doesnt start with to, then continue or go ahead
            continue
        print(line)
        
print('\nbreak\n')

#by this you can extract say a gmail id present in between the lines

with open(file_path, 'r') as files:
    for line in files:
        line = line.rstrip()
        if not '@gmail.com' in line: 
            continue
        print(line)
        
print('\nbreak\n')

fname = input('Enter a file name: ')  # Enter the path of the file
count = 0
fname = fname.replace('"', '') #what this line does is that it removes " " from the copied path because later it will be bound by " ". so to avoid "" "" to happen, we put this line
with open(fname, 'r') as files:
    for line in files:
        line = line.rstrip()
        if '@gmail.com' in line: 
            count += 1
    
print(f'There are {count} occurrences of @gmail.com in {fname}') #you can start with f so that you dont need to put commas for variables, just the {} brackets
    
#there can be people that can make an error in putting the file name
#for that you can use try and except

fnamee = input('enter the file name: ')
fnamee = fnamee.replace('"', '')
try:
    fhand = open(fnamee)
except:
    print('file cannot be opened: ', fnamee)
    quit()
    
count = 0
with open(fnamee, 'r') as files:
    for line in files:
        if line.startswith('from'):
            count += 1
print(f'there were {count} "from" lines in {fnamee}')