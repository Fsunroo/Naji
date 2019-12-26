import requests
import json
from io import open

file=open('Data.txt','r',encoding='utf-8')
key0=file.readline().rstrip()
key0=key0[1:]
key3=file.readline().rstrip()
key3=key3[1:]
key4=file.readline().rstrip()
key4=key4[1:]
key5=file.readline().rstrip()
key5=key5[1:]
key1=file.readline().rstrip()
key1=key1[1:]
key2=file.readline().rstrip()
key2=key2[1:]
key6=file.readline().rstrip()
key6=key6[1:]
url="https://api.telegram.org/bot1036599514:AAFGOOOhtpGEKfJq3aBvKeUkhnMKctU6jQg/"
money=0

def update(offset=None):
	response= requests.post(url+"GetUpdates")
	if offset:
		response= requests.post(url+"GetUpdates?&offset="+str(upd_id+1))
	content=json.loads(response.content)

	return content

def reply(text):
	response= requests.get(url+"SendMessage?chat_id="+str(chat_id)+"&text="+str(text)+"&reply_to_message_id="+str(msg_id))
	return response

upd_id=None
chmoney=""
chmoney=chmoney.encode('utf-8').decode('utf-8')
while True:
	new=update(offset=upd_id)
	if new['ok']:
		for item in new['result']:
			try:
				msg=item["message"]["text"]
				msg=msg.encode('utf-8').decode('utf-8')
				chat_id=item['message']['chat']['id']
				msg_id=item['message']['message_id']
				upd_id=item['update_id']
			except:
				msg=""
			if key0 or key3 or key4 or key5 in msg:

			    if key1 in msg:
			    	s=msg.index(key1)+len(key1)+1
			    	f=msg.index(key2)-1
			    	chmoney=msg[s:f]
			    	if "," in chmoney:
			    	    chmoney=chmoney.replace(",","")
			    	money+=int(chmoney)
		    		reply("mojudi hesab:"+str(money))
			    	pass
			    elif key6 in msg:
			    	s=msg.index(key6)+len(key6)+1
			    	f=msg.index(key2)-1
    				chmoney=msg[s:f]
			    	if "," in chmoney:
			    	    chmoney=chmoney.replace(",","")
			    	money+=int(chmoney)
			    	reply("mojudi hesab:"+str(money))
			elif msg == "Admin Mamad ZERO":
				money=0
				reply(money)

"""for item in update():
	msg=item["message"]["text"]
	msg=msg.encode('utf-8').decode('utf-8')
	chat_id=item['message']['chat']['id']
	msg_id=item['message']['message_id']
	if key0 in msg:
		s=msg.index(key1)+len(key1)+1
		f=msg.index(key2)-1
		money+=int(msg[s:f])
		reply(money)"""-