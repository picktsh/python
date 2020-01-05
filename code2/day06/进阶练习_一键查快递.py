"""
练习介绍
爬取 快递100网站 ，实现输入快递名称和单号就可以查询最新物流状态～

要求：
实现功能：用户输入快递名称和单号，程序即可在快递100https://www.kuaidi100.com/爬取最新物流状态，并将其打印出来。
"""
"""
第一步：分析需求，明确目标

实现功能：用户输入快递名称和单号，程序即可在快递100https://www.kuaidi100.com/爬取最新物流状态，并将其打印出来。
"""
"""
步骤讲解
先进入快递100https://www.kuaidi100.com/ 感受下手动搜索的流程，
如图，红框框里的是我们需要输入与想要提取的信息：
"""
"""
第二步：书写代码吧 (｡▰‿‿▰｡) ❤

如果没思路，可以偷偷看下提示哦～
"""
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
# 查询单号信息
url = 'https://www.kuaidi100.com/autonumber/autoComNum?'
text = input('输入单号，在1000+快递公司中为您智能查询')  # JDX001067991521
params = {'resultv2': '1', 'text': text}
res = requests.get(url, headers=headers, params=params)
print(res.text)
# {"comCode":"","num":"JDX001067991521","auto":[{"comCode":"jd","lengthPre":15,"noCount":1078085,"noPre":"JDX001"}]}
res1 = res.json()
if len(res1['auto']) == 0:
    print('没找到这个单号的物流信息')
elif len(res1['auto']) > 0:
    # 根据查到的单号查询物流信息
    url2 = 'https://www.kuaidi100.com/query?'
    params = {'type': str(res1['auto'][0]['comCode']),
              'postid': text,
              'temp': '0.33812520953466807',
              'phone': ''}
    res = requests.get(url2, headers=headers, params=params)
    print(res.text)
