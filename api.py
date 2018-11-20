from flask import Flask, request
from flask import abort
from flask import jsonify
app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': u'The Origins Of Freemasonry',
        'description': 'Can the ancestry of freemasonry really be...',
        'done': False
    },
    {
        'id': 2,
        'title': u'Communist Manifesto',
        'description': 'Classic of political thinking from 1848 is...',
        'done': False
    }
]

@app.route("/printdata", methods=['GET'])
def get_books(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'books': book[0]})

if __name__ == '__main__':
    app.run(debug=True)