from flask import Flask, jsonify, request
from class_try import GoodReadsAPIClient       # importing the api

app = Flask(__name__)


@app.route('/details', methods = ['POST'])    # defines the method and path to the api
def index():
    if(request.method == 'POST'):
        requestedjson = request.get_json()
        print(requestedjson['book_url'])
        # print()
        book1 = GoodReadsAPIClient(requestedjson['book_url'])
        return_from_mainapp = book1.get_book_details()   # function call with the JSON data from client POST request
        return jsonify(return_from_mainapp), 201   # converts the data from the function into JSON format and returns to the client with 201 response code.

if __name__ == '__main__':
    app.run(debug=True)