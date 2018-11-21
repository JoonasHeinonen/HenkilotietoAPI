from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response
import datetime
app = Flask(__name__)


# The following JSon is done according to instructions provided by CCMS standard.
# It will include only the required fields of Common Core.
# Link for the CCMS standard:
# https://project-open-data.cio.gov/schema/

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
        'publisher': 'Kustannusosakeyhtiö Vastapaino',
        'contact': 'Kustannusosakeyhtiö Vastapaino',
        'mbox': 'vastapaino@vastapaino.fi',
        'id': 2,
        'access': 'public'
    }
]

@app.route("/todo/api/v1.0/tasks/<int:book_id>", methods=['GET'])
def get_books(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)