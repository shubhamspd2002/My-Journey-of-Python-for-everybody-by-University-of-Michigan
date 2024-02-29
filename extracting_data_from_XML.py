#xtracting Data from XML
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Actual data: http://py4e-data.dr-chuck.net/comments_1917940.xml (Sum ends with 91)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format and Approach
#The data consists of a number of names and comment counts in XML as follows:
"""
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
"""
#You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
#To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

#counts = tree.findall('.//count')
#Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

#Sample Execution
"""
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('enter file location: ')
xml_data = urllib.request.urlopen(url).read() #to read the XML data from the URL
tree = ET.fromstring(xml_data) #to parse the XML data
counts = tree.findall('.//count') #to find all count elements

sum_counts = 0 
count_elements = 0

for count in counts: #this iterates through count elements and sum their values. 
    try:
        sum_counts += int(count.text) #to convert the char to int 
        count_elements += 1
    except:
        continue

print('Retrieving:- ', url, '\n')
print('Retrieved', len(xml_data), 'characters')
print('Count:', count_elements)
print('Sum:', sum_counts)
