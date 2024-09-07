#! python3
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4
import logging

# Configure logging.
logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s - %(message)s')

# Add headers to get better Google results.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


print('Googling...')  # Display text while downloading the Google page.

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()
logging.debug('Request status code: ' + str(res.status_code))

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.yuRUbf > div > span > a[href]')
logging.debug('Length of link Elems: ' + str(len(linkElems)))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    logging.debug('Opening link: ' + str(linkElems[i].get('href')))
    webbrowser.open(linkElems[i].get('href'))
