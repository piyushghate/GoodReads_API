import urllib.request
import xmltodict


# 12067
# 12177850
def get_authors():
    try:
        list1 = []
        for author in data['GoodreadsResponse']['book']['authors']['author']:
            list1.append(author['name'])
        return list1
        
    except :
        return data['GoodreadsResponse']['book']['authors']['author']['name']
        

with urllib.request.urlopen("https://www.goodreads.com/book/show/12067.xml?key=VugSymVo7nXix0hvwXr0w") as url:
    data = url.read()


data = xmltodict.parse(data)
# print(render_to_response('my_template.html', {'data': data}))
print(data['GoodreadsResponse']['book']['id'])

# list1 = []
# for author in data['GoodreadsResponse']['book']['authors']['author']:
#     print(author['name'])

# print(data['GoodreadsResponse']['book']['authors']['author']['name'])

title = data['GoodreadsResponse']['book']['title']
print(title)
average_rating = data['GoodreadsResponse']['book']['average_rating']
print(average_rating)
ratings_count = data['GoodreadsResponse']['book']['ratings_count']
print(ratings_count)
pages = data['GoodreadsResponse']['book']['num_pages']
print(pages)
image_url = data['GoodreadsResponse']['book']['image_url']
print(image_url)
publication_year = data['GoodreadsResponse']['book']['work']['original_publication_year']['#text']
print(publication_year)
authors = get_authors()
print(authors)

