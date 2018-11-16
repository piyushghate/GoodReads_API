import re

url = 'https://www.goodreads.com/book/show/12067.xml?key=XXX'

# pattern = re.compile(r'https://www.goodreads.com/book/show/\d')

# matches = pattern.finditer(url)

# print(matches)


# import re

# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# coreyms.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# '''

# sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'https://www.goodreads.com/book/show/\d+.', re.I)

pattern = re.compile(r'show/\d+.', re.I)

# matches = pattern.search(url)

matches = pattern.findall(url)[0]

print(matches)


#  print(matches.span())

# print (a)
# print (b)

bookID = re.compile(r'\d+', re.I)
matches2 = bookID.findall(matches)[0]
print(matches2)

# print (url[36:44])