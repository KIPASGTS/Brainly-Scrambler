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

    cookies = {

    'datadome': 'vilPngSHS4UsJutC.tSiRn5ML.yeW6fMn4E~x97O~e-Pv_8MU8uSKbAQEuRymOG6YJLQ5GPEUhNJeKKp8vBXdstgqHFJUW4o1-QDc9ROX_0hL1eUFfSUW.~p~h6gTr9'

    }

    headers = {

    'Host': 'brainly.co.id','x-b-token-long': token,'user-agent': 'Android-App 5.69.1'}

    response = requests.get('https://brainly.co.id/api/28/api_users/me', headers=headers, cookies=cookies)

    print(response.text)

def acc_check(token):

    cookies = {

    'datadome': 'vilPngSHS4UsJutC.tSiRn5ML.yeW6fMn4E~x97O~e-Pv_8MU8uSKbAQEuRymOG6YJLQ5GPEUhNJeKKp8vBXdstgqHFJUW4o1-QDc9ROX_0hL1eUFfSUW.~p~h6gTr9'

    }

    headers = {

    'Host': 'brainly.co.id','x-b-token-long': token,'user-agent': 'Android-App 5.69.1'}

    response = requests.get('https://brainly.co.id/api/28/api_users/me', headers=headers, cookies=cookies)

    print(response.text)

```
