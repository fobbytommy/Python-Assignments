# crawler

# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url), 'html.parser')


# Part I: getting all links
hrefList = []
for link in soup.find_all('a'):
	hrefList.append(str(link.get('href')))
# uncomment below statement to run part I
# pprint.pprint(hrefList)


# Part II
import re	# regular expression will be used to find address starting 'http...'
hrefDict = {}	# empty dictionary
for data in hrefList:
	match = re.search(r'http', data)
	# if we find a value that starts from 'http...',
	if match:
		# and if this value has been already in the dictionary as a key,
		if hrefDict.has_key(data):
			# then just increment its dictionary value by 1
			hrefDict[data] += 1
		else:
			# if the value is a new dictionary key then add as a key and its value set to 1
			hrefDict[data] = 1

# Part II result
pprint.pprint(hrefDict)
