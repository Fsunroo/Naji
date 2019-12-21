import requests
import json
import os
file=open('Data.txt','r')
key0=file.readline()
key1=file.readline()
key2=file.readline()
url="https://api.telegram.org/bot1036599514:AAFGOOOhtpGEKfJq3aBvKeUkhnMKctU6jQg/"

def update():
	response= requests.post(url+"GetUpdates")
	content=json.loads(response.content)
	content=content["result"]
	return content

money=0
while True:
	for item in update():
		msg=item["message"]["text"]
		if key0 in msg:
			s=msg.index(key1)+len(key1)
			f=msg.index(key2)
			money+=int(msg[s:f])
			print(money)

	pass