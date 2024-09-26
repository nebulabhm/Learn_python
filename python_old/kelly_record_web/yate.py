# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-13 12:14:19
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-19 09:08:42

from string import Template

"""
从标准库的“string”模块导入“Template”类。它支持简单的字符串替换模板
"""

"""
这个函数需要一个（可选的）字符串作为参数，用它来创建一个CGI ”content-type：“行，参数缺省值是”text/html“
"""
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

# 这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中。页面本身存储在一个单独的文件”templates/header.html“中，可以根据需要替换标题。
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title = the_title))

# 与”include_header“函数类似，这个函数使用一个字符串作为参数，来创建一个HTML页面的尾部。页面本身存储在一个单独的文件”templates/footer.html“中，参数用于动态地创建一组HTML连接标记。从这些标记的使用来看，参数应当是一个字典。
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
