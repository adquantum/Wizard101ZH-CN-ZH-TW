#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#
# 机器翻译2.0(niutrans) WebAPI 接口调用示例
# 运行前：请先填写Appid、APIKey、APISecret
# 运行方法：直接运行 main 即可 
# 结果： 控制台输出结果信息
# 
# 1.接口文档（必看）：https://www.xfyun.cn/doc/nlp/niutrans/API.html
# 2.错误码链接：https://www.xfyun.cn/document/error-code （错误码code为5位数字）
# 3.个性化翻译术语自定义：
#   登陆开放平台 https://www.xfyun.cn/
#   在控制台--机器翻译(niutrans)--自定义翻译处
#   上传自定义翻译文件（打开上传或更新窗口，可下载示例文件）
#

import re
import requests
import datetime
import hashlib
import base64
import hmac
import json
import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1.",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
def translate(text):
    class get_result(object):
        def __init__(self,host):
            # 应用ID（到控制台获取）
            self.APPID = "f46f6757"
            # 接口APISercet（到控制台机器翻译服务页面获取）
            self.Secret = "ODcxYTg1MGVjZjg2MTU2MjJmZTliY2M5"
            # 接口APIKey（到控制台机器翻译服务页面获取）
            self.APIKey= "5e6d69e673ee71004d496f8ce6dd5e54"
            
            
            # 以下为POST请求
            self.Host = host
            self.RequestUri = "/v2/ots"
            # 设置url
            # print(host)
            self.url="https://"+host+self.RequestUri
            self.HttpMethod = "POST"
            self.Algorithm = "hmac-sha256"
            self.HttpProto = "HTTP/1.1"

            # 设置当前时间
            curTime_utc = datetime.datetime.utcnow()
            self.Date = self.httpdate(curTime_utc)
            # 设置业务参数
            # 语种列表参数值请参照接口文档：https://www.xfyun.cn/doc/nlp/niutrans/API.html
            self.Text=text
            self.BusinessArgs={
                    "from": "en",
                    "to": "cn",
                }

        def hashlib_256(self, res):
            m = hashlib.sha256(bytes(res.encode(encoding='utf-8'))).digest()
            result = "SHA-256=" + base64.b64encode(m).decode(encoding='utf-8')
            return result

        def httpdate(self, dt):
            """
            Return a string representation of a date according to RFC 1123
            (HTTP/1.1).

            The supplied date must be in UTC.

            """
            weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
            month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                    "Oct", "Nov", "Dec"][dt.month - 1]
            return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
                                                            dt.year, dt.hour, dt.minute, dt.second)

        def generateSignature(self, digest):
            signatureStr = "host: " + self.Host + "\n"
            signatureStr += "date: " + self.Date + "\n"
            signatureStr += self.HttpMethod + " " + self.RequestUri \
                            + " " + self.HttpProto + "\n"
            signatureStr += "digest: " + digest
            signature = hmac.new(bytes(self.Secret.encode(encoding='utf-8')),
                                bytes(signatureStr.encode(encoding='utf-8')),
                                digestmod=hashlib.sha256).digest()
            result = base64.b64encode(signature)
            return result.decode(encoding='utf-8')

        def init_header(self, data):
            digest = self.hashlib_256(data)
            #print(digest)
            sign = self.generateSignature(digest)
            authHeader = 'api_key="%s", algorithm="%s", ' \
                        'headers="host date request-line digest", ' \
                        'signature="%s"' \
                        % (self.APIKey, self.Algorithm, sign)
            #print(authHeader)
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Method": "POST",
                "Host": self.Host,
                "Date": self.Date,
                "Digest": digest,
                "Authorization": authHeader
            }
            return headers

        def get_body(self):
            content = str(base64.b64encode(self.Text.encode('utf-8')), 'utf-8')
            postdata = {
                "common": {"app_id": self.APPID},
                "business": self.BusinessArgs,
                "data": {
                    "text": content,
                }
            }
            body = json.dumps(postdata)
            #print(body)
            return body

        def call_url(self):
            if self.APPID == '' or self.APIKey == '' or self.Secret == '':
                print('Appid 或APIKey 或APISecret 为空！请打开demo代码，填写相关信息。')
            else:
                code = 0
                body=self.get_body()
                headers=self.init_header(body)
                #print(self.url)
                response = requests.post(self.url, data=body, headers=headers,timeout=8)
                status_code = response.status_code
                #print(response.content)
                if status_code!=200:
                    # 鉴权失败
                    print("Http请求失败，状态码：" + str(status_code) + "，错误信息：" + response.text)
                    print("请根据错误信息检查代码，接口文档：https://www.xfyun.cn/doc/nlp/niutrans/API.html")
                else:
                    # 鉴权成功
                    respData = json.loads(response.text)
                    print(respData)
                    # 以下仅用于调试
                    code = str(respData["code"])
                    if code!='0':
                        print("请前往https://www.xfyun.cn/document/error-code?code=" + code + "查询解决办法")
            return json.loads(response.text)['data']['result']['trans_result']['dst']
        ##示例:  host="ntrans.xfyun.cn"域名形式
    host = "ntrans.xfyun.cn"
    #初始化类
    gClass=get_result(host)
    return  gClass.call_url()
    

# 打开文件
def translate_lang(input_file):#翻译文件中的英文部分
    file = input_file
    f = open(file, 'r', encoding='utf-16-le')
    f = f.read().splitlines()

    # 遍历每一行
    for i, line in enumerate(f):
    # 判断是否是第 3n+1 行
        if i !=0:
            if (i+1) % 3 == 1:
            # 判断行中是否包含中文
                if not (re.search(r'[\u4e00-\u9fff]', line) or re.search(r'[\u0024-\u0025]', line) or re.search(r'[\u003C-\u003E]', line)):
                    # 判断是否是空行
                    if line.strip() != "":
                    # 使用有道智云 API 翻译
                        if f[i-1]!=f[i]:
                            f[i-1]=line+f[i-1]
                        translated_line = translate(line)
                        # 将翻译后的文本写入输出文件
                        f[i] = translated_line


    with open(file,'w',encoding='utf-16 le') as f1:
        for line in f:
            f1.write(line+'\n')
def change_api(input_file):#更换翻译api，将第二行的文本翻译到第三行
    file = input_file
    f = open(file, 'r', encoding='utf-16-le')
    f = f.read().splitlines()

    # 遍历每一行
    for i, line in enumerate(f):
    # 判断是否是第 3n行
        if i !=0:
            if (i+1) % 3 == 0:
            # 判断行中是否包含中文
                if not (re.search(r'[\u4e00-\u9fff]', line) or re.search(r'[\u0024-\u0025]', line) or re.search(r'[\u003C-\u003E]', line)):
                    # 判断是否是空行
                    if line.strip() != "":
                    # 使用有道智云 API 翻译
                        print(line)
                        translated_line = translate(line)
                        # 将翻译后的文本写入输出文件
                        f[i+1] = translated_line


    with open(file,'w',encoding='utf-16 le') as f1:
        for line in f:
            f1.write(line+'\n')    
def translate_test(input_file):#测试
    file = input_file
    f = open(file, 'r', encoding='utf-16-le')
    f = f.read().splitlines()
    # 遍历每一行
    for i, line in enumerate(f):
    # 判断是否是第 3n+1 行
        if i !=0:
            if (i+1) % 3 == 1:
            # 判断行中是否包含中文
                if not (re.search(r'[\u4e00-\u9fff]', line) or re.search(r'[\u0024-\u0025]', line) or re.search(r'[\u003C-\u003E]', line)):
                # 判断是否是空行
                    if line.strip()!= "":
                    # 进行翻译
                        print(line)
#需要处理的文件列表 按下面相对路径格式写入files
files='''Release-Half-CN\Locale\English\WizQst129578.lang
'''
file_list=files.splitlines()#按行分割文件名
for line in file_list:#遍历这些文件，进行操作
    change_api(line)#调用切换翻译引擎函数，如果换成translate_lang(line)则对未翻译的英文进行补全
    print(line)
# 使用示例 需要提供输入文件的名字，作为参数。例如：
lang="Tooltips.lang"
file_path='Debug-Full-CN/Locale/English/'
input_file = file_path+lang
translate_lang(input_file)