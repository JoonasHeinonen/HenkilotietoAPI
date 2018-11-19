from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

personalData = [{'First Name' : 'Matti'}, 
            {'Last Name' : 'Meikalainen'},
            {'Phone Number' : '044 3064321'}, 
            {'Home Address' : 'Matintie 3'},
            {'Municipality': 'Turku'}, 
            {'Social Security Number' : '010100-333I'}]

@app.route("/printdata", methods=['GET'])
def printData():
    deleteData(personalData)
    return jsonify({'Personal Data' : personalData})

@app.route('/printdata', methods=['DELETE'])
def deleteData(dataName):
    dataArray = [array for array in personalData if array['Social Security Number'] == dataName]
    personalData.remove(dataArray[0])
    return jsonify({'Personal Data' : personalData})

if __name__ == '__main__':
    app.run(debug=True)