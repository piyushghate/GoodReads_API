try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import urllib.request


url = 'https://www.goodreads.com/book/show/12177850.xml?key=XXX'

tree = ET.parse(urllib.request.urlopen(url))

root = tree.getroot()
print(root.tag)