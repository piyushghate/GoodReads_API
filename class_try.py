import urllib.request
import re
from hold_key import GoodReads_key      # key saved in different file
import xmltodict


class GoodReadsAPIClient:

    def __init__(self, url):
        self.url = url                  # Url from user
        self.title = None
        self.average_rating = None
        self.ratings_count = None
        self.pages = None
        self.image_url = None
        self.publication_year = None
        self.authors = None
       
    def get_book_details(self):

        def get_authors():
            try:           # if output from below code is list/array    
                list1 = []
                for author in data['GoodreadsResponse']['book']['authors']['author']:
                    list1.append(author['name'])
                return (', '.join(list1))
        
            except :        # if output from below code is string
                return data['GoodreadsResponse']['book']['authors']['author']['name']

        pattern = re.compile(r'https://www.goodreads.com/book/show/\d+[.-]', re.I)
        matches = pattern.search(self.url)      # search for the above pattern in url

        if (matches):       # if its a valid url
            matches2 = pattern.findall(self.url)[0]     # returns the string with the match
            
            # get the number(bookid) from returned string
            bookID = re.compile(r'\d+', re.I)           
            matches3 = bookID.findall(matches2)[0]      

            url1 = "https://www.goodreads.com/book/show/"+matches3+".xml?key="+GoodReads_key

            with urllib.request.urlopen(url1) as url:   
                xmldata = url.read()       # content from webpage to data

            data = xmltodict.parse(xmldata)    # convert the xml content to dictionary

            #  get the required text from the dictionary
            self.title = data['GoodreadsResponse']['book']['title']
            self.average_rating = data['GoodreadsResponse']['book']['average_rating']
            self.ratings_count = data['GoodreadsResponse']['book']['ratings_count']
            self.pages = data['GoodreadsResponse']['book']['num_pages']
            self.image_url = data['GoodreadsResponse']['book']['image_url']
            self.publication_year = data['GoodreadsResponse']['book']['work']['original_publication_year']['#text']
            self.authors = get_authors()

            # dict holding the above content and converting to the required format
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