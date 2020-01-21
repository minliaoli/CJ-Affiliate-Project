from flask import Flask
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/testAlg')
def testAlg():
    keywords = ["sports", "trash", "electronics"]
    return keywords[random.randint(0, 2)]

@app.route('/test/<data>', methods=['GET', 'POST'])
def test(data):
    if data == 'data is true' : 
        return 'true'
    if data =='data' :
        return 'yes but'
    return 'false'

@app.route('/alg/<inputData>', methods=['GET'])
def runAlg(inputData):
    if inputData == testInput : 
        return '200 true we goodie'

if __name__ == "__main__":
    app.run()
