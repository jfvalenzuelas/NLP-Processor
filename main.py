import requests
import utils

url, user, password = utils.loadAccessData("ServiceNow");
headers = {"Content-Type":"application/json","Accept":"application/json"}

url += '/tweets?processed=false&language=en&topic=corona_virus'

response = requests.get(url, auth=(user, password), headers=headers, json={"system": "JFVS1993"})

if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())

data = response.json()

print(len(data))

processed_tweets = []

for record in data:
    