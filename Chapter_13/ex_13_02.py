import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
# URL for testing is http://py4e-data.dr-chuck.net/comments_42.json

uh = urllib.request.urlopen(url)
print('Retrieving', url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
# print(data.decode())


info = json.loads(data)
# print(json.dumps(info, indent=2))
# print('Item count:', len(info))

count = 0
i = 0
total = 0

for item in info["comments"]:
    # print('Count', info["comments"][i]["count"])
    count = count + 1
    total = total + info["comments"][i]["count"]
    i = i + 1

print('Count', count)
print('Sum:', total)
