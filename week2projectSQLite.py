import sqlite3

conn = sqlite3.connect('week2project.sqlite') #name of the file we have created. after running successfully, open SQLite, go to home section and in the search box, search for this file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ') #if u enter a new file and u r still seeing old data in sqlite, just refresh. here u can enter the path link directly
fname = fname.replace('"', '')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email_org = pieces[1]
    main = email_org.split('@')
    domain = main[-1] #When we use parts[-1], it's a shorthand way of accessing the last element of the list parts. -1 is an index that refers to the last element of a list or array in Python. -2 would refer to the second-to-last element, -3 to the third-to-last element, and so forth.
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,)) #this line in ' ' is the SQL code to extract data to make database in SQLite
    row = cur.fetchone()
    if row is None: #if that email has 0 counts:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,)) #add 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,)) #this ? is a placeholder to make sure to not allow SQL injection. (email,) is a tuple with one component only. this tuple will replace ?
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
