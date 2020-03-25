import requests
import json

url = 'http://192.168.113.133/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

# 有些信息不需要认证，可以直接访问, 如软件版本号
# data = {
#     "jsonrpc": "2.0",             # 固定值
#     "method": "apiinfo.version",  # 方法
#     "params": [],                 # 参数
#     "id": 1                       # 随便给个数字，表示作业号
# }

# 获取令牌
# e979f6a6c7e4da4d5d60a92661034042
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }

# 获取所有的主机信息
# 'hostid': '10084'
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤，取出满足条件的主机
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#             ]
#         }
#     },
#     "auth": "e979f6a6c7e4da4d5d60a92661034042",
#     "id": 1
# }

# 删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         # "13",
#         "10084"  # hostid = 10084
#     ],
#     "auth": "e979f6a6c7e4da4d5d60a92661034042",
#     "id": 1
# }

# 获取Linux servers组的id
# 'groupid': '2'
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "e979f6a6c7e4da4d5d60a92661034042",
#     "id": 1
# }

# 获取Template OS Linux的模板id
# 'templateid': '10001'
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "e979f6a6c7e4da4d5d60a92661034042",
#     "id": 1
# }

# 创建名为nsd1910web1的主机，属于Linux Servers组，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1910web1",
        "interfaces": [  # 使用什么方式监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.113.133",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "e979f6a6c7e4da4d5d60a92661034042",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())   # 重点关心的是返回值的result
