from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {
        "id": 1,
        "title": "A Song of Ice and Fire - A Game of Thrones",
        "autor": "George R. R. Martin"
    },
    {
        "id": 2,
        "title": "Angels and Demons",
        "autor": "Dan Brown"
    },
    {
        "id": 3,
        "title": "Harry Potter And The Sorcerer's Stone",
        "autor": "J. K. Rowling",  
    },
]

@app.route('/books', methods=['GET'])
def getBooks():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def getBooksById(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books', methods=['POST'])
def createBook():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods=['PUT'])
def updateBook(id):
    new_book = request.get_json()
    for book in books:
        if book.get('id') == id:
            book.update(new_book)
    return jsonify(new_book)

@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)
            
app.run(host="localhost", port=8080, debug=True)