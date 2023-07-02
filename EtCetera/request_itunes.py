import json
import requests
import sys

if len(sys.argv)!= 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(response.json())
#python convert the response into dictonary
#To format in better manner we import json

# print(json.dumps(response.json(),indent =2))

#Now if we want to print specific item

o = response.json()
for result in o["results"]:
    print(result["trackName"])