# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# test URL is http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL: ')
times = input('Enter count: ')
rtimes = int(times)
position = input('Enter position: ')
rposition = int(position)

for i in range(1, rtimes + 1):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    print('Retrieving:', tags[rposition - 1].get('href', None))
    url = tags[rposition - 1].get('href', None)
