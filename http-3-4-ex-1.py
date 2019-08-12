import requests
import re

pattern = r"<a href=[\"|\']([\w:\.\/]*)[\"|\']>[\w\sа-яА-Я]*?</a>"

start_url = input()
end_url = input()

res = requests.get(start_url)

gr = re.findall(pattern, str(res.content))
for i in range(len(gr)):
    res = requests.get(gr[i])
    sec = re.findall(pattern, str(res.content))
    if end_url in sec:
        answer = 'Yes'

print(answer)
