import urllib.request
from xml.dom import minidom
import re
from hold_key import GoodReads_key

def get_book_details(user_passed_url):

    pattern = re.compile(r'show/\d+.', re.I)
    matches = pattern.findall(user_passed_url)[0]
    bookID = re.compile(r'\d+', re.I)
    matches2 = bookID.findall(matches)[0]
    
    # print("BookID: ",matches2)

    url = "https://www.goodreads.com/book/show/"+matches2+".xml?key="+GoodReads_key

    # print("url: ",url)

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

    return book

print(get_book_details("https://www.goodreads.com/book/show/12067.Good_Omens"))

