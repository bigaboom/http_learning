import re
import requests

pattern = r"<a(?:[\w =\'\"&?.:\/,;\(\)\s\[\]\+]*)?\s?(?:href(?:\s)?=(?:\s)?(?:[\"\']?))(?:[a-zA-Z\-]*:\/\/)?([a-zA-Z]{1}[a-zA-Z0-9.-]*)(?:[\w]*\/\s)*(?:[\"\']?)(?:[\w =\[\]\+\'\"&?.:\/,;\(\)а-яА-Я\s-]*)?>"
ended = []
link = input()
links_ended = []

req = requests.get(link)
links = re.findall(pattern, str(req.text))

for link in links:
    #print(link)
    if (link not in links_ended) and (link not in ['..','.']) and (link[-5:] != '.html') and (link[-4:] != '.htm'):
        links_ended.append(link)
    #print(link[5])

links_ended.sort()
for i in links_ended:
    print(i)