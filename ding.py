import json
import requests

url = '丁丁机器人的api地址'
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",  # 发送消息类型为文本
#     "text": {
#         "content": 'test text',  # 消息正文
#     },
#     "at": {
#         "atMobiles": ['1383551xxxx'],
#         "isAtAll": False,  # 是否@所有人
#     }
# }


data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"zabbix报警",
         "text": "## zabbix报警\n" +
                 "> ![screenshot](https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=848361732,4071536337&fm=26&gp=0.jpg)\n"  +
                 "> ###### 10点20分发布 [报警信息](http://www.xxxxxx.com) \n"
     },
    "at": {
        "atMobiles": [
            # "156xxxx8827",
            # "189xxxx8325"
        ],
        "isAtAll": 'false'
    }
 }
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
