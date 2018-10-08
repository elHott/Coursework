# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# test at http://py4e-data.dr-chuck.net/comments_42.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0
# Retrieve all of the cells in a table
cells = soup('span')
for cell in cells:
    # Look at the parts of a table cell
    # print('CELL:', cell)
    # print('URL:', cell.get('href', None))
    # print('Contents:', cell.contents[0])
    # print('Attrs:', cell.attrs)
    count = count + 1
    total = total + int(cell.contents[0])

print('Count', count)
print('Sum', total)
