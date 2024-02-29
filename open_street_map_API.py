import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ') #put here Ann Arbor, MI
    if len(address) < 1: break #if u just press enter without putting anything, this loop will break

    address = address.strip()
    parms = dict()
    parms['q'] = address #to do the q=query thing shown in the screenshot

    url = serviceurl + urllib.parse.urlencode(parms) #or this thing does the fancy stuff of q=query for u

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx) #to ignore certificates problem
    data = uh.read().decode() #to retrieve the raw data and since after retriving, the raw data is in UTF8, we gotta decode it to unicode and then put it in data variable. 
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    #print(data)
    
    try:
        js = json.loads(data) #to parse the data. data can only be parsed in pyhthon in unicode form and not UTF8
    except:
        js = None

    #print(js) 
    
    if not js or 'features' not in js: #this is to check whether 'features' exist
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    #print(json.dumps(js, indent=4)) #unhash this to see the JSON data

    lat = js['features'][0]['properties']['lat'] #what rhis tells that in js dictionary, search for 0th object of 'features' and  in 'features' look for 'properties' and in 'properties', look for 'lat' and take its value and put it in lat variable  
    lon = js['features'][0]['properties']['lon'] #to parse the longitude. same logic as above
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted'] #same as lat
    print(location)
