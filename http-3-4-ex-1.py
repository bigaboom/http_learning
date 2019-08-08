import requests
import re

pattern = r"<a href=(\"|\')([\w:\.\/]*)(\"|\')>[\w\sа-яА-Я]*?</a>"

#s = '<a href="http:\\\\www.google.com">Здрасте мордасте</a>'

#gr = re.match(pattern, s)
#print('1111')
#print(gr.group(2))
#print('2222')

res = requests.get("https://stepic.org/media/attachments/lesson/24472/sample0.html")
print(res.status_code)
print(res.content)

gr = re.search(pattern, str(res.content))
print(gr.group(2))