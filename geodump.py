#in this we are going to link the universities with their respective co-ordinates (latitude and longitude). the co-ordinates are saved
#present in the mock geoapi app by py4e. you have to parse that json data from mock geoappi and link it. by running this,
# on the geoapi mock map, the location will be shown


import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
ah = r"C:\Users\LENOVO\Desktop\opengeo\where.js"
rh = ah.replace('"', '')
fhand = codecs.open(rh, 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if len(js['features']) == 0: continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

