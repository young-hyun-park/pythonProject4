import urllib.request, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_list = list()
count = 0
url = 'http://py4e-data.dr-chuck.net/comments_997806.json'

data = urllib.request.urlopen(url,context=ctx).read()

info = json.loads(data)
for item in info['comments']:
    data_list.append(item['count'])
for i in data_list:
    count = count + i
print(count)