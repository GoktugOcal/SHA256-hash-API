# SHA256-hash-API
A web service for SHA256 hash digest

> **info**
> Developed by Göktuğ Öcal

## Usage

The app is created with Flask and runs on Render.com publicly. The url of the REST API is https://sha256-api.onrender.com . There are two functions in the API. One is POST for sending a text to convert to SHA256 hash format and other is GET for gathering hash format to string format if the string format is stored beforehand.

### POST

```console
$ python request.py -r POST -m <string>
```

```console
$ python request.py -r POST -m goktugocal
e683c3e863b1718963a6.....
```

### GET
```console
$ python request.py -r GET -m <hash_string>
```

```console
$ python request.py -r GET -m e683c3e863b1718963a6.....
goktugocal
```

## Additional Questions

### How can you scale your implementation?
> If we think this REST API will face with huge traffic a distributed system with a single or multiple load balancers could be useful for balancing all the requests to multiple servers.

### How did you deploy this application?
> I have used a free-to-use service which is Render.com for that deployment. I have uploaded my FLASK service with some requirements to the github and connected it to render.com. Then started the Flask service with gunicorn on the cloud.

### How can you improve this process and make it easy to maintain?
> I can use a serverless cloud service for deployment and use storage services to store string-hash pairs.