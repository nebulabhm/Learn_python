'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-11-19 11:04:19
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-12-11 10:46:49
FilePath: \Learn_python\python_exercise\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

url = url + urllib.parse.quote('白居易')

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

import urllib.request

url = "https://www.nasdaq.com/market-activity/index/ndx/historical"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url = url, headers=headers)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    print(htmlstr)




