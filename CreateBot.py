import requests, random, string, threading, re
#pip install requests
def genRandom(leng):
	char_set = string.ascii_uppercase + string.digits
	return ''.join(random.sample(char_set*6, leng))

def macc():
    email = genRandom(28) + '@gmail.com' #bisa di ubah
    nick = genRandom(6) + 'botbyKIPAS' #bisa di ubah
    headers = {'Host': 'brainly.co.id','content-length': '346','user-agent': 'Mozilla/5.0 (Linux; Android 10; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','sec-ch-ua-platform': 'Android','origin': 'https://brainly.co.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://brainly.co.id/signup?entry=1','cookie': 'G_ENABLED_IDPS=google'}
    data = '{"operationName":"registerUser","variables":{"nick":"' + nick + '","country":"ID","entry":"1","email":"' + email + '","password":"yah9898@","dateOfBirth":"2001-01-01","acceptedTermsOfService":true,"accountType":null},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f737c8e219ac6f050068332b108c70b28a1062722fd6458fe8b49489c9603ca1"}}}'
    response = requests.post('https://brainly.co.id/graphql/id', headers=headers, data=data).text
    if '"validationErrors":null' in response:
    	token = re.findall('{"token":"(.*?)"', response)[0]
    	xd = open('brainlybot.txt', 'a+')
    	xd.write('Email: ' + email + ' Password: yah9898@ Token: (' + token + ')\n')
    	xd.close()
    	print('[BRAINLY] Email: ' + email + ' Password: yah9898@ Token: (' + token + ')')
    else:
    	print('failed')
    	
for i in range(0,100000):
	t = threading.Thread(target=macc)
	t.start()
