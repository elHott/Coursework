import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter URL: ')
# URL for testing is http://py4e-data.dr-chuck.net/comments_42.xml

uh = urllib.request.urlopen(url)
print('Retrieving', url)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))

total = 0
for count in tree.iter('count'):
    total = total + int(count.text)

print('Sum:', total)
