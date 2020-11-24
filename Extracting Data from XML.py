import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count_list = list()
count_sum = 0

url = ' http://py4e-data.dr-chuck.net/comments_997805.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)

comments = tree.find('comments')
comment = comments.findall('comment')
for i in comment:
    count = i.findall('count')
    count_list = count_list + count
for i in count_list:
    count_sum = count_sum + int(i.text)
print(count_sum)