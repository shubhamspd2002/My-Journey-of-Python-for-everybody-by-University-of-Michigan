#Following Links in Python
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Fedora.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: R
#Strategy: The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Function to follow links in the specified position for a given number of times
def follow_links(url, count, position):
    for i in range(count):
        print("extrating from:", url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        anchor_tags = soup('a') #find all anchor tags
        href_values = [tag.get('href', None) for tag in anchor_tags]  #extract the href values from anchor tags
        nxt_url = href_values[position - 1]  #get the next URL based on the specified position entered by the user
        url = nxt_url  #update the current URL for the next iteration

    return url

start_url = input("Enter URL: ")
iteration_count = int(input("Enter count: "))
position_to_follow = int(input("Enter position: "))

#call the function to follow links and print the last retrieved url
last_url = follow_links(start_url, iteration_count, position_to_follow) 
print("Last name retrieved from the final page:", last_url.split('_')[-1].split('.')[0])
