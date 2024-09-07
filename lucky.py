#! python3
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

print('Googling...')  # Display text while downloading the Google page.

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result.
linkElems = soup.select('span > a[href]')
#linkElems = soup.findAll('a', {'jsname': 'UWckNb'})
logging.debug('Length of link Elems: ' + str(len(linkElems)))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    logging.debug('Opening search result...')
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
