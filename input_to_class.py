from class_try import GoodReadsAPIClient


# "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"
# "https://www.goodreads.com/book/show/12067.Good_Omens"

input_from_user = input('Please mention a valid GoodReads url for book info: ') # input from user

book1 = GoodReadsAPIClient(input_from_user)     # initializing the class with book1 instance

print(GoodReadsAPIClient.get_book_details(book1))   # calling the method inside of the class