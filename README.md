# Brainly-Scrambler

```
Untuk admin brainly jangan lupa pasang captcha mu
````

Note: Kamu harus bikin bot account dulu untuk mendapatkan token

- Set Https Proxy
```python
import os
os.environ['HTTPS_PROXY'] = os.environ['https_proxy'] = 'http://ip:port/'
```

# requirement
- requests
```
pip install requests
```

# action
- Token Checker
```python
def acc_check(token):
    cookies = {'datadome': 'vilPngSHS4UsJutC.tSiRn5ML.yeW6fMn4E~x97O~e-Pv_8MU8uSKbAQEuRymOG6YJLQ5GPEUhNJeKKp8vBXdstgqHFJUW4o1-QDc9ROX_0hL1eUFfSUW.~p~h6gTr9'}
    headers = {'Host': 'brainly.co.id','x-b-token-long': token,'user-agent': 'Android-App 5.69.1'}
    response = requests.get('https://brainly.co.id/api/28/api_users/me', headers=headers, cookies=cookies)
    print(response.text)
```
- Follow User
```python
def follow(token,userid):
    cookies = {'datadome': 'nvAnnuA9Ov9qRyjv-dg99xa_eW-O0lLjG59loLw.ZjbeZAoixKmSW9qDnZ-wIFOEYMw.9sr6S1FOLLRtA7g~SxpcbhveJ8A9DQRZVF2on4mPcHDrE1nazwTYWuQy8Hx',}
    headers = {'Host': 'brainly.co.id','user-agent': 'Android-App 5.69.1','x-b-token-long': token,'accept': 'application/json'}
    response = requests.put('https://brainly.co.id/api/28/api_users/follow/' + str(userid), headers=headers, cookies=cookies).text
    if '"success":true' in response:
    	print('[BOT] success follow the user')
    else:
    	print('Failed to follow user')
```
- Create question
```python
def genRandom(leng):
	char_set = string.ascii_uppercase + string.digits
	return ''.join(random.sample(char_set*6, leng))

def msoal(token):
    cookies = {'datadome': genRandom(9) + '-2shclUzf_ZfansDAwMNmquiuxoksG_JgOSTM597sgnJJ.BntlJefemRKCogmA7i~' + genRandom(10) + '~bglWfaB8uYSsOBlEHHIJ1tLsXUsAsMssXc9QfBc03r'}
    headers = {'Host': 'brainly.co.id','x-b-token-long': token,'accept': 'application/json','user-agent': 'Android-App 5.69.1','content-type': 'application/json; charset=UTF-8','content-length': '219'}
    data = '{"attachments":[],"content":"MESSAGE","points":10,"subject_id":2}'
    response = requests.post('https://brainly.co.id/api/28/api_tasks/add', headers=headers, cookies=cookies, data=data).text
    if '"is_deleted":false' in response:
    	print('[SOAL] Success Token: ' + token)
    else:
    	print('Failed')
```
