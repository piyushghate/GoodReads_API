import urllib.request
import re
from hold_key import GoodReads_key
import xmltodict


class GoodReadsAPIClient:

    def __init__(self, url):
        self.url = url
        self.title = None
        self.average_rating = None
        self.ratings_count = None
        self.pages = None
        self.image_url = None
        self.publication_year = None
        self.authors = None
       
    def get_book_details(self):

        # print(self.url)
        # print(type(self.url))
        def get_authors():
            try:
                list1 = []
                for author in data['GoodreadsResponse']['book']['authors']['author']:
                    list1.append(author['name'])
                return (', '.join(list1))
        
            except :
                return data['GoodreadsResponse']['book']['authors']['author']['name']

        # pattern = re.compile(r'show/\d+.', re.I)
        pattern = re.compile(r'https://www.goodreads.com/book/show/\d+[.-]', re.I)
        matches = pattern.search(self.url)

        if (matches):
            matches2 = pattern.findall(self.url)[0]
            bookID = re.compile(r'\d+', re.I)
            matches2 = bookID.findall(matches2)[0]
            
            # print("BookID: ",matches2)

            url1 = "https://www.goodreads.com/book/show/"+matches2+".xml?key="+GoodReads_key

            with urllib.request.urlopen(url1) as url:
                data = url.read()

            data = xmltodict.parse(data)

            self.title = data['GoodreadsResponse']['book']['title']
            self.average_rating = data['GoodreadsResponse']['book']['average_rating']
            self.ratings_count = data['GoodreadsResponse']['book']['ratings_count']
            self.pages = data['GoodreadsResponse']['book']['num_pages']
            self.image_url = data['GoodreadsResponse']['book']['image_url']
            self.publication_year = data['GoodreadsResponse']['book']['work']['original_publication_year']['#text']
            self.authors = get_authors()

            book = {
                'title': self.title,
                'average_rating': float(self.average_rating),
                'ratings_count': int(self.ratings_count),
                'num_pages': int(self.pages),
                'image_url': self.image_url,
                'publication_year': self.publication_year,
                'authors': self.authors,
            }

            return book


        else:
            return "InvalidGoodreadsURL"



# "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"
# "https://www.goodreads.com/book/show/12067.Good_Omens"

input_from_user = input('Please mention a valid GoodReads url for book info: ')
book1 = GoodReadsAPIClient(input_from_user)

print(GoodReadsAPIClient.get_book_details(book1))