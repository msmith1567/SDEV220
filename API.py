from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (list to store book data)
books = []

# Helper function to find a book by ID
def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

# CREATE a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()

    if not all(k in data for k in ('id', 'book_name', 'author', 'publisher')):
        return jsonify({"error": "Missing required fields"}), 400

    if find_book(data['id']):
        return jsonify({"error": "Book with this ID already exists"}), 400

    books.append(data)
    return jsonify({"message": "Book created successfully", "book": data}), 201

# READ all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# READ a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

# UPDATE a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = find_book(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    # Update fields if provided
    book['book_name'] = data.get('book_name', book['book_name'])
    book['author'] = data.get('author', book['author'])
    book['publisher'] = data.get('publisher', book['publisher'])

    return jsonify({"message": "Book updated successfully", "book": book}), 200

# DELETE a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)