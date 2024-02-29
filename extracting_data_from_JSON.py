#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the 
#comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#Actual data: http://py4e-data.dr-chuck.net/comments_1917941.json (Sum ends with 73)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student 
# will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format: The data consists of a number of names and comment counts in JSON as follows:
'''
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''

#Sample Execution:
'''
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''

import urllib.request
import json

url = input('Enter location: ')
print('Retrieving:-', url)

try:
    r = urllib.request.urlopen(url)
    data = r.read().decode()
    json_data = json.loads(data)
    comments = json_data['comments']

    count = len(comments)
    total_sum = sum(comment['count'] for comment in comments)

    print('Retrieved', len(data), 'characters')
    print('Count:', count)
    print('Sum:', total_sum)
    
except Exception as e:
    print('an error occured:', e)

