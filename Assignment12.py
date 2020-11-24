from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
sum = 0
contents_list = list()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    contents_list.append(tag.contents[0])
for i in contents_list:
    sum = int(i) + sum
print(sum)