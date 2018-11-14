import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')

# print(tree)

root = tree.getroot()

# print(root)

# print(root.tag)

# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# for movie in root.iter('movie'):
#     print(movie.attrib)


# for description in root.iter('description'):
#     print(description.text)

print("------")

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)