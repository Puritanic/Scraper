import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://old.reddit.com/r/ProgrammerHumor/"
request = urllib.request.Request(url, headers={
                                 'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, 'html.parser')
# First lets get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div", attrs={'id': 'siteTable'})
# Now we go into main_table and get every a element in it which has a class "title"
links = main_table.find_all("a", class_="title")
# List to store a dict of the data we extracted
extracted_records = []
for link in links:
    title = link.text
    url = link['href']
    # There are better ways to check if a URL is absolute in Python. For sake simplicity we'll just stick to .startwith method of a string
    # https://stackoverflow.com/questions/8357098/how-can-i-check-if-a-url-is-absolute-using-python
    if not url.startswith('http'):
        url = "https://old.reddit.com/"+url
    # You can join urls better using urlparse library of python.
    # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin
    # Lets just print it
    print("%s - %s" % (title, url))
    record = {
        'title': title,
        'url': url
    }
    extracted_records.append(record)
# Lets write these to a JSON file for now.
with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile)
