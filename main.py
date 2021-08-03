from ast import parse
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# parse the HTML 
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify) 
# html tree traversal 
title = soup.title #get the title of html page
# print(type(soup))
# print(type(title))
# print(type(title.string))
#get all the anchors of the html page
anchors = soup.find_all('a')
# print(anchors)

#get all the paragraphs of the html page
paras  = soup.find_all('p')
# print(paras)

# get class of any element of the html page  
# print(soup.find('p')['class'])

# find all the element with class lead  
# print(soup.find_all('p', class_ = "leadget"))

# get the text from the tag/soup  
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the links on the page:

anchors = soup.find_all('a')
all_links  = set()
for link in anchors:
    if(link.get('href') != '#'):
        linktext = "https://www.codewithharry.com/" +link.get('href')
        all_links.add(link)
        # print(linktext)

# comments 
markup = "<p><!-- This is comment --></p>"
soup2 = BeautifulSoup(markup)
# print(soup2.p.string)

# .content = A tag's children are available as a list.
# .children = A tag's children are available as a generator. 

navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
# for elem in navbarSupportedContent.contents:
    # print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# find for navbar  

for item in navbarSupportedContent.parents:
     print(item.name)