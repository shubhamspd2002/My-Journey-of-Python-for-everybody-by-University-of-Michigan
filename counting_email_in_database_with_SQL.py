#the aim of this code is to store the data in the sql database by using python code

import sqlite3

conn = sqlite3.connect('emaildb.sqlite') #name of the file we have created. after running successfully, open SQLite, go to home section and in the search box, search for this file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ') #if u enter a new file and u r still seeing old data in sqlite, just refresh. here u can enter the path link directly
fname = fname.replace('"', '')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #this line in ' ' is the SQL code to extract data
    row = cur.fetchone()
    if row is None: #if that email has 0 counts:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,)) #add 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,)) #this ? is a placeholder to make sure to not allow SQL injection. (email,) is a tuple with one component only. this tuple will replace ?
        conn.commit() #The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed. 

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
