import urllib.request
from xml.dom import minidom

url = 'https://www.goodreads.com/book/show/12177850.xml?key=VugSymVo7nXix0hvwXr0w'

dom = minidom.parse(urllib.request.urlopen(url))

title = dom.getElementsByTagName('title')[0]
average_rating = dom.getElementsByTagName('average_rating')[0]
ratings_count = dom.getElementsByTagName('ratings_count')[1]
pages = dom.getElementsByTagName('num_pages')[0]
image_url = dom.getElementsByTagName('image_url')[0]
publication_year = dom.getElementsByTagName('original_publication_year')[0]
authors = dom.getElementsByTagName('name')[0]

book = {
    'title': title.firstChild.data,
    'average_rating': float(average_rating.firstChild.data),
    'ratings_count': int(ratings_count.firstChild.data),
    'num_pages': int(pages.firstChild.data),
    'image_url': image_url.firstChild.data,
    'publication_year': publication_year.firstChild.data,
    'authors': authors.firstChild.data,
}

print(book)