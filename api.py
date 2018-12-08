from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import url_for
import datetime
app = Flask(__name__)

#########################################################################
# The following JSon is done according to instructions provided by CCMS #
# standard. It will include only the required fields of Common Core.    #
# Link for the CCMS standard: https://project-open-data.cio.gov/schema/ #
#########################################################################

books = [
    {
        'title': u'The Origins Of Freemasonry',
        'description': 'Can the ancestry of freemasonry really be...',
        'keyword': 'Freemasonry',
        'modified': datetime.datetime(2018, 11, 21),
        'publisher': 'University Of Pennsylvania Press',
        'contact': 'University Of Pennsylvania Press',
        'mbox': 'ips@ingramcontent.com',
        'id': 1,
        'access': 'public'

    },
    {
        'title': u'Kommunistinen Manifesti',
        'description': 'Poliittisen ajattelun klassikko vuodelta 1848...',
        'keyword': 'Communism',
        'modified': datetime.datetime(2018, 11, 21),
        'publisher': 'Kustannusosakeyhtio Vastapaino',
        'contact': 'Kustannusosakeyhtio Vastapaino',
        'mbox': 'vastapaino@vastapaino.fi',
        'id': 2,
        'access': 'public'
    }
]

@app.route("/")
@app.route("/books")
def home():
    return render_template('home.html', title='Home')

@app.route("/books/all", methods=['GET'])
def get_all_books():
    return jsonify({'book': books})

@app.route("/books/<int:book_id>", methods=['GET'])
def get_books(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'title': request.json['title'],
        'description': request.json['description'],
        'keyword': request.json['keyword'],
        'modified': datetime.datetime.now(),
        'publisher': request.json['publisher'],
        'contact': request.json['contact'],
        'mbox': request.json['mbox'],
        'id': books[-1]['id'] + 1,
        'access': request.json['access']
    }
    books.append(book)
    return jsonify({'book': book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) != unicode:
        abort(400)
    if 'keyword' in request.json and type(request.json['keyword']) != unicode:
        abort(400)
    if 'publisher' in request.json and type(request.json['publisher']) != unicode:
        abort(400)
    if 'contact' in request.json and type(request.json['contact']) != unicode:
        abort(400)
    if 'mbox' in request.json and type(request.json['mbox']) != unicode:
        abort(400)
    if 'access' in request.json and type(request.json['access']) != unicode:
        abort(400)
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['description'] = request.json.get('description', book[0]['description'])
    book[0]['keyword'] = request.json.get('keyword', book[0]['keyword'])
    book[0]['publisher'] = request.json.get('publisher', book[0]['publisher'])
    book[0]['contact'] = request.json.get('contact', book[0]['contact'])
    book[0]['mbox'] = request.json.get('mbox', book[0]['mbox'])
    book[0]['access'] = request.json.get('access', book[0]['access'])
    return jsonify({'book': book[0]})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})

def make_public_book(book):
    new_book = {}
    for field in book:
        if field == "id":
            new_book['uri'] =url_for('get_book', book_id=book['id'], _external=True)
        else:
            new_book[field] = book[field]
    return new_book

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)