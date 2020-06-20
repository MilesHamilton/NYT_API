from flask import Flask, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import Books

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<id>', methods=['GET', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Books.get(Books.id == id)))
        else:
            bookList = []
            for book in Books.select():
                bookList.append(model_to_dict(book))
            return jsonify(bookList)

    if request.method == 'POST':
        new_book = dict_to_model(Books, request.get_json())
        new_book.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True)
