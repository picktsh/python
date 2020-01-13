"""
练习介绍
学了爬虫这么久，想不想接触下AI，创建一个可以聊天的机器人呀٩̋(๑˃́ꇴ˂̀๑)

要求：
实现功能：利用图灵机器人官网http://www.tuling123.com/的接口，创建一个可以聊天的机器人
"""
"""
第一步：登录注册图灵机器人

注册登录，才能创建自己的图灵机器人。
根据帮助中心的“说明书”，我们可以了解如何运用这个新工具～
文档地址: https://www.kancloud.cn/turing/www-tuling123-com/718227
"""
import requests
import json

url = 'http://openapi.tuling123.com/openapi/api/v2'
data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "b13f44a2adc54a64b760b396afaf4e77",
        # "apiKey": "0ac325b4dad74f38830b24cb5fc1ced6",
        "userId": "136311"
    }
}
res = requests.post(url, data=data)
if res.status_code == 200:
    print(res.text)
else:
    print('请求失败!', url)
