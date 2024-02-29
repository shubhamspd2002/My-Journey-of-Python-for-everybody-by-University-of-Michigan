#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#Data Format: The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:
#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
#<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter - ') #you enter this http://py4e-data.dr-chuck.net/comments_1917938.html

html = urllib.request.urlopen(url).read() #read the HTML from the URL

soup = BeautifulSoup(html, 'html.parser') #parse the HTML using beautifulsoup

span_tags = soup('span') #extract all of the span tags

total_sum = 0 # Initialize sum variable


for span_tag in span_tags: #loop through the span tags, extract content, convert to integer, and then add to the sum
    number_text = span_tag.contents[0] #extract the text of span tag
    number = int(number_text) #convert text to an integer which is an important step
    total_sum += number
print("Sum:", total_sum)
