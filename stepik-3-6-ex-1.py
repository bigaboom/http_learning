import requests

params = {
    'json' : 'true'
}

#n = input('Number: ')


with open("dataset_24476_3.txt", "r") as f:
    n = [int(line.strip()) for line in f]

    for i in n:
        link = 'http://numbersapi.com/' + str(i) + '/math?json=true'
        req = requests.get(link, params)
        data = req.json()

        if data['found'] == True:
            print("Interesting")
        else:
            print("Boring")