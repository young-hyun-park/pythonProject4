import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
contents_list = list()
final = list()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/known_by_Nodoka.html"

for i in range(8):
    count = 0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url_split = url.split('_')
    contents_list.append(url_split[2])
    for tag in tags:
        count = count + 1
        if count == 18:
            url = tag.get('href',None)

for i in contents_list:
    x = i.split('.')
    final.append(x[0])
print(final)