from flask import Flask
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
import categorize
import json
import urllib.parse



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

#The route t handle URLs
@app.route('/url/<path:urlStr>', methods=['GET'])
def url(urlStr):
    print(   urllib.parse.unquote(urlStr)   )
    if "youtube.com" in urlStr:
        rawTranscript = youtubeTranscript(urlStr)
        return categorize.function_a(rawTranscript,2)
    else:
        theURL=urllib.parse.unquote(urlStr)
        #return ('[{"id":"5e3a7cc8f125753e48b6b499","link":"https://www.hotels.com/ho1123568864/hotel-baghan-ortaca-turkey/?wapb1=hotelcontentfeed","title":"Hotel Baghan","description":"When you stay at Hotel Baghan in Ortaca, youll be 10 minutes by car from Alexandria Train Station. Featured amenities include a 24-hour front desk, luggage storage, and laundry facilities.","advertiserName":"Hotels.com","price":{},"catalogId":"6630","imageLink":"https://media.expedia.com/hotels/36000000/35090000/35080300/35080277/270b2409_b.jpg","categoryName":null,"categoryName2":"Business","categoryName1":"Recreation","categoryName3":"Home"},{"id":"5e3a7cc8f125753e48b6b49b","link":"https://www.hotels.com/ho717811136/hotel-grand-nubra-leh-india/?wapb1=hotelcontentfeed","title":"Hotel Grand Nubra","description":"When you stay at Hotel Grand Nubra in Leh, youll be 5 minutes by car from Diskit Monastery. Featured amenities include limo/town car service, a 24-hour front desk, and luggage storage. A train station pick-up service is available for a surcharge.","advertiserName":"Hotels.com","price":{},"catalogId":"6630","imageLink":"https://media.expedia.com/hotels/23000000/22410000/22400400/22400348/f7b6e9a9_b.jpg","categoryName":null,"categoryName2":"Fashion","categoryName1":"Recreation","categoryName3":"Business"},{"id":"5e3a7cc8f125753e48b6b4d8","link":"https://www.tours4fun.com/swiss-winter-holiday-murren-schilthorn-4-day.html?utm_source=cj&utm_medium=affiliate&utm_campaign=feed","title":"4-Day Swiss Winter Holiday in Murren: Cable Car to Schilthorn | Brunch at Piz Gloria","description":"The package includes transfers from international airports in Zurich and Geneva to the station in Murren as part of SBB&#039;s Swiss Transfer Ticket service.To redeem the train transfer, you must show your printed transfer validation at the international airport information desk in Zurich or Geneva during opening hours:- Visitor&#039;s Centre, Geneva Airport: Daily 7:00am - 11:00pm- Airport Information Service Centre, Zurich Airport: Daily 6:00am - 11:30pmUpon showing your printed transfer validation at one of the information desks above, you will receive your complete travel kit including train tickets and hotel vouchers.DO NOT wait for a driver at the airport! If you are arriving the same day, you must collect your luggage and proceed directly to one of the information desks listed above to collect your train ticket and travel kit, after which you may proceed to the train station to begin your incredible journey to Murren.Once you arrive at Murren you may proceed directly to the hotel. Earliest check-in is 2:00pm.","advertiserName":"Tours4Fun","price":{},"catalogId":"8778","imageLink":"https://d3ne5s9fv9p81l.cloudfront.net/images/201907091562691164_5d24c65cedc5f_watermark_800_800.jpg","categoryName":null,"categoryName2":"Business","categoryName1":"Recreation","categoryName3":"Home"},{"id":"5e3a7d1bf125753e48b6bcad","link":"https://www.barnesandnoble.com/w/credit-card-rebate-get-an-unfair-advantage-with-credit-card-rebate-when-you-get-this-guide-on-cash-back-credit-cards-credit-card-rewards-cash-rebate-cards-and-more-steve-d-knight/1113652537?ean=2940013559035","title":"Credit Card Rebate; Get An Unfair Advantage With Credit Card Rebate When You Get This Guide On Cash Back Credit Cards, Credit Card Rewards, Cash Rebat","description":"Do you want to understand how credit card rebates work?    Would you like to earn the maximum rebates possible of off the credit cards you have?   Are you interested in learning about the different kinds of rebates, so you can find the one that fits your lifestyle and spending habits?    This book will teach you all of this and more!    Credit Card Rebate explains how rebates work and how credit card companies can even afford to pay them to you.  It explains how to read your credit card statements carefully in order to figure out how much you are getting in rebates and how you can strategically use your credit card to earn even more.   Most of us have credit cards that we use on a regular basis, but don&#x2019;t take the time to research the rebates and rewards that are available to us.   As you read this book and learn about the different kinds of rebates, you will discover which ones best fits your lifestyle.   You can then transfer your balance to that kind of credit card if you don&#x2019;t have it already and begin to earn cash back and rewards on purchases you&#x2019;re making already!         If you learn to spend wisely and use credit card rebates for regular purchases such as gas, groceries and other travel expenses, you&#x2019;ll be surprised to discover how your credit card is now earning cash for you.   Here is list of the chapter title included in this book.   Look at some of the information you can&#x2019;t afford to miss:Chapter 1: Understanding Rebate Credit CardsChapter 2: Credit Card Rebates &#x2013; How They WorkChapter 3: Credit Card Rebates - How To Get YoursChapter 4: Credit Card Rebates & RewardsChapter 5: Credit Card Rebates - Finding the Right CardChapter 6: Cash Rebate Credit CardChapter 7: Credit Card Rebates Rule The RoostChapter 8: Credit card rebates and rewardsChapter 9: Credit Card Rebates - Offer the Best BenefitsChapter 10: Credit Card Rebates &#x2013; What They Mean to You Chapter 11: Credit Card Rebates OverviewGet the best credit card rebate today!","advertiserName":"Barnes & Noble","price":{},"catalogId":"5879","imageLink":"https://prodimage.barnesandnoble.com/pimages/2940013559035_p0_v1_s192x300.jpg","categoryName":"Media > Books","categoryName2":"Games","categoryName1":"Home","categoryName3":"Business"}]\n')
        # return "Yes We get: "+urlStr
        if theURL:
            return categorize.function_a(theURL,1)
        else: 
            print("Not working??????")
        return theURL

@app.route('/test/<data>', methods=['GET', 'POST'])
def test(data):
    if data == 'data is true' : 
        return 'true'
    if data =='data' :
        return 'yes but'
    return 'false'

@app.route('/alg/<inputData>', methods=['GET'])
def runAlg(inputData):  
    if inputData:
        return categorize.function_a(inputData,0)
    else: 
        print("Not working??????")

def youtubeTranscript(youtubeURL):
    video_id = youtubeURL[32:]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    raw = ""
    for x in transcript:
        if "[" not in x['text']: #gets rid of [Music], [Applause], etc....
            raw += x['text'] + " "
    return raw
if __name__ == "__main__":
    app.run(host= '0.0.0.0')
