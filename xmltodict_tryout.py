import urllib.request
import xmltodict


with urllib.request.urlopen("https://www.goodreads.com/book/show/12067.xml?key=VugSymVo7nXix0hvwXr0w") as url:
            data = url.read()


data = xmltodict.parse(data)
# print(render_to_response('my_template.html', {'data': data}))
print(data['GoodreadsResponse']['book']['id'])

list1 = []
for author in data['GoodreadsResponse']['book']['authors']['author']:
    print(author['name'])

# print(data['GoodreadsResponse']['book']['authors']['author']['name'])