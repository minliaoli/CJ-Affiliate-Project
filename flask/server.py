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
    if inputData == 'This is a blog about sports.' : 
        return '[{"class":"Sports","name":"Basketball","brand":"Nike","detail":"The Nike® Elite Championship Official Basketball features a soft premium touch which is ideal for indoor play. Your championship season starts with the Nike® Elite Championship Official Basketball.","id":"5dd6d1bb9363073f74b393a9"},{"class":"Sports","name":"Basketball","brand":"Adidas","detail":"ALL-COURT BASKETBALL A DURABLE BASKETBALL FOR ALL SURFACES. Whether it\'s on the hardwood or the pavement, this ball has one thing on its mind: getting to the basket. The ball is stitched with a durable synthetic leather cover that makes it perfect for both indoor and outdoor courts.","id":"5dd6d26d9363073f74b393aa"},{"class":"Sports","name":"UA Project Rock 2","brand":"Under Armour","detail":"Project Rock is not a brand, it’s a movement. It’s a core belief, that I 100% don’t care what color you are, how old you are, where you come from or what you do for a living. The only thing I care about is you and me, building the belief that regardless of whatever the odds, we can overcome and achieve—but it all starts with the work we’re willing to put in with our two hands.","id":"5dd6d2cf9363073f74b393ab"},{"class":"Technology","name":"MX Master Wireless Mouse","brand":"Logitech","detail":"High-Precision Sensor, Speed-Adaptive Scroll Wheel, Easy-Switch up to 3 Devices","id":"5dd6d3259363073f74b393ac"},{"class":"Technology","name":"Dell 24 Gaming Monitor","brand":"Dell","detail":"Slay any beast with your very own. Dominate with tear-free visuals enabled by NVIDIA® G-Sync™ compatible monitor.","id":"5dd6d3849363073f74b393ad"},{"class":"Politics","name":"The Audacity of Hope","brand":"Book","detail":"The Audacity of Hope: Thoughts on Reclaiming the American Dream by Barack Obama","id":"5dd6d3ed9363073f74b393ae"}]'
        
if __name__ == "__main__":
    app.run()
