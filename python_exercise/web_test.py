'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-11-19 20:18:06
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-11-19 21:57:45
FilePath: \Learn_python\python_exercise\web_test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests

url = 'https://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.google.com"
}

response = requests.get(url, headers=headers)

print(response.text)

import urllib.request

# 定义一个 URL
url = "https://www.baidu.com/"

# 写一个请求头，用一个字典表示，格式如下：
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36 Edg/111.0.1661.62"
}

# 创建一个请求对象，注意这里的headers一定要用关键字参数
request = urllib.request.Request(url, headers=headers)

# 打开 URL 并返回一个类文件对象
response = urllib.request.urlopen(request)

# 读取并打印出 URL 的内容
html = response.read().decode('utf-8')
print(html)

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                  "Safari/537.36 Edg/111.0.1661.62"
}

url = url + urllib.parse.quote('周杰伦')

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf‐8'))

from urllib.parse import urlencode
params = {"name": "张三", "age": 18, "gender": "male"}
query = urlencode(params)
print(query)

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'
keyword = input('hello')

# 这里的data是我浏览器上的，要用你自己的表单数据来填，找表单数据的方法上面已经写过了
data = {
    'from': 'en',
    'to': 'zh',
    'query': keyword,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'a7e3ffc10673738961631bc32b623f57',
    'domain': 'common'
}

data = urllib.parse.urlencode(data)
url = url + data

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
    'cookie': 'BAIDU_WISE_UID=wapp_1698434084817_353; BIDUPSID=8C459FF47BAEABAED3CBAD69EFB6E338; PSTM=1698591300; delPer=0; PSINO=7; __bid_n=18cb07304617456693d080; BAIDUID=5CB218C3AA9F721A0AD743BDDCD84CB9:FG=1; BAIDUID_BFESS=5CB218C3AA9F721A0AD743BDDCD84CB9:FG=1; BDUSS=zFGZjRSMDBlZWdMTW9oaC1QenhkMm84YUF0Sm02amtrc01WZTR2dkUwOFE1TmxsRUFBQUFBJCQAAAAAAAAAAAEAAAAH5~sObmVidWxhYmhtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBXsmUQV7Jld; BDUSS_BFESS=zFGZjRSMDBlZWdMTW9oaC1QenhkMm84YUF0Sm02amtrc01WZTR2dkUwOFE1TmxsRUFBQUFBJCQAAAAAAAAAAAEAAAAH5~sObmVidWxhYmhtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBXsmUQV7Jld; ZFY=8iY0zoLsbCdY9YXG1Tgfywxb0puJ6yCoVLyxDmOYwEI:C; BCLID=11660661663607431566; BDSFRCVID=n6LOJeC627lZIcJtzM3PI7dOEhKZcuoTH6_nZ1HGfeULr8tQVRf0EG0Pgf8g0KF-QIByogKKQmOTHAuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRItoIDMtI83qn7I5bJHK4QHbxoXK-r054o2WDvaBqbcOR5Jj6K--4t1Qx6JXfTjHmKfVPoG-q3BHU3-3MA-BPCAK4nUWIr4QC392b5gQhr4sq0x05QWe-bQyPQ3JPJDLIOMahvlal7xOhjGQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3WjjT0eHLHt6KDf5vfL5rbMJRjqn8k-PnVeUQXqtnZKxtqtJvQhqTJWtb08DOLyjJfXULJyn62-4RnWncdWfFhWp3tef5sK67M0qKwbG3405OT5KFO0KJc3j6GOqowhPJvyp_DXnO73RQlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVDKXtC_hMCDr5nJbqRthhMbe5K62aKDsWDQ1BhcqEIL4jPvAyttp5h6uJhOAJKn9KRncyJOhDUbSjln_W6_nQUj-Lx7HfTnI-foDtp5nhMJTb67JDMPzqJQA3Jcy523ibR6vQpnNfqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHHLDJ5Dt3J; BCLID_BFESS=11660661663607431566; BDSFRCVID_BFESS=n6LOJeC627lZIcJtzM3PI7dOEhKZcuoTH6_nZ1HGfeULr8tQVRf0EG0Pgf8g0KF-QIByogKKQmOTHAuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JRItoIDMtI83qn7I5bJHK4QHbxoXK-r054o2WDvaBqbcOR5Jj6K--4t1Qx6JXfTjHmKfVPoG-q3BHU3-3MA-BPCAK4nUWIr4QC392b5gQhr4sq0x05QWe-bQyPQ3JPJDLIOMahvlal7xOhjGQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3WjjT0eHLHt6KDf5vfL5rbMJRjqn8k-PnVeUQXqtnZKxtqtJvQhqTJWtb08DOLyjJfXULJyn62-4RnWncdWfFhWp3tef5sK67M0qKwbG3405OT5KFO0KJc3j6GOqowhPJvyp_DXnO73RQlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVDKXtC_hMCDr5nJbqRthhMbe5K62aKDsWDQ1BhcqEIL4jPvAyttp5h6uJhOAJKn9KRncyJOhDUbSjln_W6_nQUj-Lx7HfTnI-foDtp5nhMJTb67JDMPzqJQA3Jcy523ibR6vQpnNfqQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHHLDJ5Dt3J; ZD_ENTRY=bing; RT="z=1&dm=baidu.com&si=07a89b01-ad44-421a-9d95-7b15a92e0b3d&ss=m3lhdhqh&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3juu&ul=5ayuj&hd=5ayuw"; H_PS_PSSID=60277_61027_61055_61099_60853_61124_61127_61140_61150_61175; BA_HECTOR=8420ak2480ak808k0h842k8g8u69hs1jjp37a1v'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf‐8'))