import requests
import json

res = {}
bdays = []

client_id = '0ad502220aeb121ef3de'
client_secret = 'c26b8ef879d0d653660d72bb513ad1bb'

token_link = 'https://api.artsy.net/api/tokens/xapp_token'

token_params = {
    'client_id' : client_id,
    'client_secret' : client_secret
}

token_req = requests.post(token_link, token_params)
j = json.loads(token_req.text)
token = j['token']

header = {'X-Xapp-Token' : token}


with open('dataset_24476_4.txt', 'r') as f:
    lines = [l.strip() for l in f]
    print(lines)

#lines = ['4d8b92b34eb68a1b2c0003f4', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']

for l in lines:
    link = 'https://api.artsy.net/api/artists/' + l
    #print(link)
    req = requests.get(link, headers = header)
    j = json.loads(req.text)
    if int(j['birthday']) not in bdays:
        bdays.append(int(j['birthday']))
    if int(j['birthday']) not in res.keys():
        res[int(j['birthday'])] = [j['sortable_name']]
    else:
        res[int(j['birthday'])].append(j['sortable_name'])
    #print(j)

bdays.sort()
for i in bdays:
    names = res[i]
    names.sort()
    for j in names:
        print(j)

#print(res)