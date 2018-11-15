try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import urllib.request

import xmltodict

import re


url = 'https://www.goodreads.com/book/show/12177850.xml?key=VugSymVo7nXix0hvwXr0w'

tree = ET.parse(urllib.request.urlopen(url))

root = tree.getroot()
print(root.tag)



# for elem in root.iter('book/authos/author'):
#     # print (elem.tag)
#     # print(elem.attrib)
#     # print(elem)
#     name = elem.find('name')
#     print(name)

# for node in tree.findall('.//book/authors/author/name'):
#     if (tree.findall('.//book/authors/author/name/role/')):
#         print (node.tag) 
#         print (node.attrib)
#         print (node.text) 


# re.search( r'<role/>', node, re.M|re.I)

o = xmltodict.parse(tree)