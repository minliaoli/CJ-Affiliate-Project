from flask import Flask
from flask_cors import CORS
#from parse_Offer import function_a
#
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
    if inputData == 'This is a blog.' : 
        return '[{"id":"5e2f84d9373a5e0a80934add","link":"https://www.hotels.com/ho275670/city-park-hotel-residence-poznan-poland/?wapb1=hotelcontentfeed","title":"City Park Hotel & Residence","description":"With a stay at City Park Hotel & Residence in Poznan (Grunwald), you\'ll be within a 5-minute drive of Poznan Palm House and Parish of St. Stanislaus Kostka. Featured amenities include complimentary wired Internet access, a business center, and limo/town car service. For a surcharge, guests may use a roundtrip airport shuttle (available 24 hours) and a train station pick-up service.","advertiserName":"Hotels.com","price":{},"catalogId":"6434","imageLink":"https://media.expedia.com/hotels/3000000/2230000/2228000/2227922/d1f35bf5_b.jpg","categoryName":null},{"id":"5e2f84d9373a5e0a80934bf7","link":"https://www.joybuy.com/654020562.html","title":"Parent-child Swimsuit Leaf Print Halter Bikini Set Mommy Daughter Swimwear","description":"Parent-child Swimsuit Leaf Print Halter Bikini Set Mommy Daughter Swimwear","advertiserName":"JD.com","price":{},"catalogId":"7334","imageLink":"http://img13.360buyimg.com/ecps/s150x104_jfs/t1/61989/13/7096/71058/5d53e50aE188a835a/a4777705b4a040dc.jpg"},{"id":"5e2f84d9373a5e0a80934c27","link":"https://www.joybuy.com/652725261.html","title":"Best Daddy Mommy Newborn Infant Baby Boys Girls Summer Romper Bodysuit Jumpsuit Clothes Outfits","description":"Best Daddy Mommy Newborn Infant Baby Boys Girls Summer Romper Bodysuit Jumpsuit Clothes Outfits","advertiserName":"JD.com","price":{},"catalogId":"7334","imageLink":"http://img10.360buyimg.com/ecps/s150x104_jfs/t1/71738/7/1234/115591/5cf7d0cbE17ebf511/1d536bb23429082f.jpg"},{"id":"5e2f84d9373a5e0a80934e0b","link":"https://www.joybuy.com/651810021.html","title":"Mother Daughter Dresses Summer   Casual Dress Parent-child Outfit Clothes","description":"Mother Daughter Dresses Summer   Casual Dress Parent-child Outfit Clothes","advertiserName":"JD.com","price":{},"catalogId":"7334","imageLink":"http://img10.360buyimg.com/ecps/s150x104_jfs/t30079/263/742177772/46387/54033964/5bfd01d9Ne32954cf.jpg","categoryName":"Apparel & Accessories > Clothing"},{"id":"5e2f84d9373a5e0a80935ab5","link":"https://www.barnesandnoble.com/w/credit-card-concepts-sam-ghosh/1130819048?ean=2940156006748","title":"Credit Card Concepts Sam Ghosh Author","description":"The biggest reason for making Credit Card mistakes and ending up with bad credit is the lack of knowledge&nbsp;about Credit Card including the fees and charges. Imprudent use of Credit Cards can have serious long term impact on our financial. With this book, we are trying to present the different facets of Credit Card ownership.","advertiserName":"Barnes & Noble","price":{},"catalogId":"5879","imageLink":"https://prodimage.barnesandnoble.com/pimages/2940156006748_p0_v1_s192x300.jpg","categoryName":"Media > Books"}]'
    #return function_a(inputData)   
if __name__ == "__main__":
    app.run()
