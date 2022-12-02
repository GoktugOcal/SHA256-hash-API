import requests

url = 'http://127.0.0.1:5000/messages'
myobj = "goktugocal"

x = requests.post(url, json = myobj)

print(x.text)