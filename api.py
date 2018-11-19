from flask import Flask, jsonify, request
app = Flask(__name__)

personalData = [{'First Name' : 'Matti', 
            'Last Name' : 'Meikalainen',
            'Phone Number' : '044 3064321', 
            'Home Address' : 'Matintie 3',
            'Municipality': 'Turku', 
            'Social Security Number' : '010100-333I'}]

@app.route("/", methods=['GET'])
def printData():
    return jsonify({'Personal Data' : personalData})

if __name__ == '__main__':
    app.run(debug=True)