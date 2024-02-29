#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not 
# append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
#basically what program wants is that make a list of words from romeo.txt, so that the words that have been repeated in romeo.txt (like 'and', 'is')
# do not repeat in the list that you have made. Also sort them at the end.

fname = input("Enter file name: ")
fname = fname.replace('"', '')
fh = open(fname)
lst = list()
for line in fh: 
    wrds = line.rstrip().split() #to remove all the spaces and bring them in a single line, then split them and store in wrds variable
    for word in wrds: #itteration variable 'word' to access each split element in wrds
        if word not in lst: #In other words, this also says that if it is in the list, continue
            lst.append(word) #to attach every new word in the lst
lst.sort()   #sort them lexicographically
print(lst)

