"""
练习介绍
想不想自己动手做个翻译器呢，一点都不难哦～
就用你学过的post和json，一起试试爬取有道翻译自制翻译器吧ლ(＾ω＾ლ)

要求
实现功能：用户输入英文或中文，程序即可打印出来对应的译文。
"""
"""
第一步：分析问题，明确目标
实现功能：用户输入英文或中文，程序即可打印出来对应的译文。
"""
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
while True:
    i = input('请输入要翻译的内容:(q:退出)')
    if i == 'q':
        break
    # i = '日本'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15789232174317',
        'sign': '26367ef747166d23c38407b3dbf8c1b3',
        'ts': '1578923217431',
        'bv': '75a84f6fbcebd913f0a4e81b6ee54608',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    res = requests.post(url, headers=headers, data=data)
    # print(res.text)
    result = json.loads(res.text)
    """
    {'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 1, 'translateResult': [[{'src': '日本', 'tgt': 'Japan'}]]}
    """
    print(result)
    type = result['type'].split("2")
    res_list = result['translateResult'][0]
    # print(res_list)
    for i in res_list:
        # print(i)
        print('{}: {}'.format(type[0], i['src']))
        print('{}: {}'.format(type[1], i['tgt']))
print('程序结束')
