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
- Auto Answer News Question
```python
import requests, json, re, threading, random, string, time

def genRandom(leng):
	char_set = string.ascii_uppercase + string.digits
	return ''.join(random.sample(char_set*6, leng))

def jawab(token, soalid):
    cookies = {'datadome': '1-mQuyPhpoAw3yXBBrcqPP9A_r_PKNrW8L'+ genRandom(8) + '.q4P8q730KdirMtno41eT5qvWLyou~ZhXq' + genRandom(12) + '-.lH1D6Z0nNizpX3G3o' + genRandom(6) + 'qqBF-ZpY'}
    headers = {'Host': 'brainly.co.id','user-agent': 'Android-App 5.69.1','x-b-token-long': token,'accept': 'application/json','content-type': 'application/json; charset=UTF-8','content-length': '111','accept-encoding': 'gzip'}
    data = '{"attachments":[],"content":"<p><strong>Jawaban:</strong></p><p>AUTO ANSWER BY KIPASGTS</p>","task_id":' + str(soalid) + '}'
    response = requests.post('https://brainly.co.id/api/28/api_responses/add', headers=headers, cookies=cookies, data=data).text
    if '"success":true' in response:
    	print('[ANSWER] SUCCES TO ANSWER TASKID: ' + str(soalid) + ' TOKEN: ' + token)
    else:
    	pass
    	
def getSoal(token):
    
    cookies = {'datadome': 'VfvClQqTG4qrAtoEaysFFVHD6_M5L8hznfRV3LWQDsKw9gXEsGLUTXYM2~bll.GU.-' + genRandom(12) + '_' + genRandom(14) + '-i8wHTlvM.D1PxL4j7kEcpbRxghHKn~guv'}
    headers = {'Host': 'brainly.co.id','accept': 'application/json','x-apollo-operation-id': genRandom(9) + '636db5f80e1b3d62cc79f9c7c87fb181995e4f54e00c73c2' + genRandom(7),'x-apollo-operation-name': 'FeedQuestionsQuery','x-apollo-cache-key': genRandom(5) + 'df6e8c90d9da697beca294' + genRandom(5),'x-apollo-cache-fetch-strategy': 'NETWORK_ONLY','x-apollo-expire-timeout': '0','x-apollo-expire-after-read': 'false','x-apollo-prefetch': 'false','x-apollo-cache-do-not-store': 'false','x-b-token-long': token,'user-agent': 'Android-App 5.69.1','content-type': 'application/json; charset=utf-8','content-length': '811'}
    data = '{"operationName":"FeedQuestionsQuery","variables":{"first":10,"gradeIds":[],"subjectIds":[],"status":"ANSWER_NEEDED","feedType":"PUBLIC"},"query":"query FeedQuestionsQuery($first: Int, $before: ID, $gradeIds: [Int], $subjectIds: [Int], $status: FeedQuestionStatusFilter, $feedType: FeedType) { feed(first: $first, feedType: $feedType, before: $before, status: $status, gradeIds: $gradeIds, subjectIds: $subjectIds) { __typename edges { __typename node { __typename ...StreamQuestionFragment } cursor } pageInfo { __typename endCursor hasNextPage hasPreviousPage } } } fragment StreamQuestionFragment on Question { __typename databaseId content isReported created author { __typename nick avatar { __typename thumbnailUrl } } created pointsForAnswer attachments { __typename url } subject { __typename name } }"}'
    response = requests.post('https://brainly.co.id/graphql/id?operationName=FeedQuestionsQuery', headers=headers, cookies=cookies, data=data).text
    if '{"url":"h' in response:
    	print('Captcha Detected, Change your ip!')
    	ur = re.findall('"(.*?)"', response)[1]
    	os._exit(0)
    else:
    	soal = re.findall('"databaseId":(.*?),', response)
    	t = threading.Thread(target=jawab, args=(token, soal[0]))
    	t.start()
    	
a = open('brainlybot.txt', 'r').read()
for i in a.split('\n'):
	if len(i) != 0:
		token = i.split('Token: (')[1].split(')')[0]
		t = threading.Thread(target=getSoal, args=[token])
		t.start()
		time.sleep(3)
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
