#This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:
'''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
'''
# #If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.
# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. The ZIP file contains the tracks.csv file to be used for this assignment. You can export your own tracks from iTunes and create a database, but for the database that you turn in for this assignment, only use the tracks.csv data that is provided. You can adapt the tracks_csv.py application in the zip file to complete the assignment.
# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

'''
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
'''

#The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)


# Track	                                    Artist	    Album	        Genre
# Chase the Ace	                            AC/DC       Who Made Who	Rock
# D.T.	                                    AC/DC	    Who Made Who	Rock
# For Those About To Rock (We Salute You)	AC/DC	    Who Made Who	Rock

import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

path = input('Enter file name: ')  # download file here https://www.py4e.com/code3/tracks/ and input the file path
handlee = path.replace('"', '')
handle = open(handlee)

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,GenreName
#   0                          1      2           3  4   5        6

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7:
        continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre_name = pieces[6]

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES (?)''', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)''', 
        (name, album_id, genre_id, length, rating, count))

    conn.commit()