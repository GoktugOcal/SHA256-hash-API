import requests
import argparse
 
 
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--request", required=True, type=str, help = "Request Method (GET, POST)")
parser.add_argument("-m", "--message", required=True, type=str, help = "Message to send")
args = parser.parse_args()

message = args.message

if args.request == "POST":
    url = 'https://sha256-api.onrender.com/messages'
    x = requests.post(url, json = message)
    print(x.text)

elif args.request == "GET":
    url = 'https://sha256-api.onrender.com/messages/' + message
    x = requests.get(url)
    print(x.text)
    
else: print("Please enter a valid method...")
