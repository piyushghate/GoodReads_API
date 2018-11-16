import urllib.request
import re
from hold_key import GoodReads_key
import xmltodict


def get_book_details(user_passed_url):
    
    def get_authors():
        try:
            list1 = []
            for author in data['GoodreadsResponse']['book']['authors']['author']:
                list1.append(author['name'])
            return list1
        
        except :
            return data['GoodreadsResponse']['book']['authors']['author']['name']

    # pattern = re.compile(r'show/\d+.', re.I)
    pattern = re.compile(r'https://www.goodreads.com/book/show/\d+[.-]', re.I)
    matches = pattern.search(user_passed_url)

    if (matches):
        matches2 = pattern.findall(user_passed_url)[0]
        bookID = re.compile(r'\d+', re.I)
        matches2 = bookID.findall(matches2)[0]
        
        # print("BookID: ",matches2)

        url1 = "https://www.goodreads.com/book/show/"+matches2+".xml?key="+GoodReads_key

        with urllib.request.urlopen(url1) as url:
            data = url.read()

        data = xmltodict.parse(data)

        title = data['GoodreadsResponse']['book']['title']
        average_rating = data['GoodreadsResponse']['book']['average_rating']
        ratings_count = data['GoodreadsResponse']['book']['ratings_count']
        pages = data['GoodreadsResponse']['book']['num_pages']
        image_url = data['GoodreadsResponse']['book']['image_url']
        publication_year = data['GoodreadsResponse']['book']['work']['original_publication_year']['#text']
        authors = get_authors()

        book = {
            'title': title,
            'average_rating': float(average_rating),
            'ratings_count': int(ratings_count),
            'num_pages': int(pages),
            'image_url': image_url,
            'publication_year': publication_year,
            'authors': authors,
        }

        return book


    else:
        return "InvalidGoodreadsURL"



print(get_book_details("https://www.goodreads.com/book/show/12067.Good_Omens"))