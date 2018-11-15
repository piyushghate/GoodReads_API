import urllib.request
import xmltodict


with urllib.request.urlopen("https://www.goodreads.com/book/show/12177850.xml?key=VugSymVo7nXix0hvwXr0w") as url:
            data = url.read()


data = xmltodict.parse(data)
# print(render_to_response('my_template.html', {'data': data}))
print(data[GoodreadsResponse][Request])