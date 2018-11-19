# from class_try import GoodReadsAPIClient


# # "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"
# # "https://www.goodreads.com/book/show/12067.Good_Omens"

# input_from_user = input('Please mention a valid GoodReads url for book info: ') # input from user

# book1 = GoodReadsAPIClient(input_from_user)     # initializing the class with book1 instance

# print(book1.get_book_details())   # calling the method inside of the class



import requests
import json

# making a post request @http://127.0.0.1:5000/repos with header as ({'Content-Type': 'application/json'}) and data as ({'org': 'google'})
r = requests.post('http://127.0.0.1:5000/details', data=json.dumps({'book_url': 'https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire'}), headers={'Content-Type': 'application/json'})

print(r)            # to check the status code 
print(r.headers)    # to print the header info
print(r.content)