import requests
import re
import sys
import uuid
import requests
import hashlib
import time

import time

import importlib
importlib.reload(sys)



YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '57cfbb59561dca3d'
APP_SECRET = '4I0TTNsl8891zFNl1e6id186L7XSspUR'
def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def translate(text):
  # 将需要翻译的文本填入代码中的 "待输入的文字"
  q = text
  # 将源语言和目标语言填入代码中的 "源语言" 和 "目标语言"
  data = {}
  data['from'] = 'en'
  data['to'] = 'zh-CHS'
  data['signType'] = 'v3'
  curtime = str(int(time.time()))
  data['curtime'] = curtime
  salt = str(uuid.uuid1())
  signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
  sign = encrypt(signStr)
  data['appKey'] = APP_KEY
  data['q'] = q
  data['salt'] = salt
  data['sign'] = sign

  # 发送请求并解析响应结果
  response = do_request(data)
  result = response.json()
  # 返回翻译结果
  return result['translation'][0]

print(translate('Maxine Rockhoppierre'))