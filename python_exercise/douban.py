'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-11-18 14:31:38
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-11-18 14:31:45
FilePath: \Learn_python\python_exercise\douban.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests # 导入requests库，这个库用来发送请求
from lxml import etree # 这个用来解析html的
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
# 发送请求


count = 1
with open("douban_movieTop250.txt",'w') as fw:
    for i in range(0,250,25):
        url = f'https://movie.douban.com/top250?start={i}'
        print(url)
        time.sleep(2)
        content = requests.get(url,headers=headers)
        #返回网页内容解析城html标准格式
        html = etree.HTML(content.text)
        titles = html.xpath("//div[@class='hd'][1]//span[@class='title'][1]/text()")# 获取所有标题名称，返回list
        for j in titles:
            fw.write(f"{count},{j}\n")
            count += 1