import urllib.request
# import xml.etree.ElementTree as ET
from xml.dom import minidom

# import xmltodict

url = 'https://www.goodreads.com/book/show/12177850.xml?key=XXX'

# with urllib.request.urlopen("https://www.goodreads.com/book/show/12177850.xml?key=VugSymVo7nXix0hvwXr0w") as url:
    # data = url.read()

dom = minidom.parse(urllib.request.urlopen(url))


# data = xmltodict.parse(data)
# print(render_to_response('my_template.html', {'data': data}))
# print(data[GoodreadsResponse][Request])

# tree = ET.parse(data)



# tree = ET.ElementTree(data)

# root = tree.getroot()

# print(root.tag)

# print(root.attrib)

# print(root)


# dom = minidom.parse(data)

title = dom.getElementsByTagName('title')[0]
print('title: ',title.firstChild.data)
average_rating = dom.getElementsByTagName('average_rating')[0]
print('average_rating: ', average_rating.firstChild.data)
ratings_count = dom.getElementsByTagName('ratings_count')[1]
print('ratings_count: ', ratings_count.firstChild.data)
pages = dom.getElementsByTagName('num_pages')[0]
print('num_pages: ', pages.firstChild.data)
image_url = dom.getElementsByTagName('image_url')[0]
print('image_url: ', image_url.firstChild.data)
publication_year = dom.getElementsByTagName('original_publication_year')[0]
print('publication_year: ', publication_year.firstChild.data)
authors = dom.getElementsByTagName('name')[0]
print('authors: ', authors.firstChild.data)


# publication_year = dom.getElementsByTagName('work')
# for years in publication_year:
#     pyears = years.getElementsByTagName('publication_year')
#     print('publication_year: ', pyears)