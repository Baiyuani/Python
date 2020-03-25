import requests

url = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
headers = {'Authorization': 'APPCODE 你的APPCODE'}
params = {'citycode': '101010300'}
r = requests.get(url, headers=headers, params=params)
print(r.json())
