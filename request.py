import requests

url = 'http://sha256-api.onrender.com:5000/messages'
myobj = "goktugocal"

x = requests.post(url, json = myobj)


# hashed = "e683c3e863b1718963a6ce705d8f8d821330540c3584b9d8d253cf2c6fe9d792"
# url = 'http://127.0.0.1:5000/messages/' + hashed
# x = requests.get(url)


print(x.text)