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

print('\033[34m# ' * 11)
print('# 欢迎使用 小P 机器人 #')
print('# ' * 11, '\033[0m')
url = 'http://openapi.tuling123.com/openapi/api/v2'
# 返回结果的样例
echo = {
    'emotion': {
        'robotEmotion': {
            'a': 0,
            'd': 0,
            'emotionId': 0,
            'p': 0
        },
        'userEmotion': {
            'a': 0,
            'd': 0,
            'emotionId': 0,
            'p': 0
        }
    },
    'intent': {
        'actionName': '',
        'code': 10004,
        'intentName': ''
    },
    'results': [
        {
            'groupType': 1,
            'resultType': 'text',
            'values': {
                'text': '聪明又善解人意的小Q就是我了'
            }
        }
    ]
}
while True:
    text = input('想对我说点什么呢?(输入 q 退出)')
    if text == 'q':
        break
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                # "text": '你叫什么呀'
                "text": text
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
            # "apiKey": "b13f44a2adc54a64b760b396afaf4e77",
            "apiKey": "0ac325b4dad74f38830b24cb5fc1ced6",
            "userId": "136311"
        }
    }
    
    res = requests.post(url, data=json.dumps(data))
    if res.status_code == 200:
        # print(res.text)
        res_json = json.loads(res.text)
        res_list = res_json['results']
        for r in res_list:
            print('\033[34m小P: \033[32m{} \033[0m'.format(r['values']['text']))
    else:
        print('\033[31m 请求失败! \033[0m', url)
print('拜拜啦!下次再玩')
