# -*- coding: UTF-8 -*-
import requests
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import json
import random
trendweight = {}
trendweight["Fashion"]= 1
trendweight["Recreation"] = 1
trendweight["Sports"] = 1
trendweight["Games"] = 1
trendweight["Health"] = 1
trendweight["Home"] = 1
trendweight["Business"] = 1
trendweight["Technology"] = 1
trendweight["Society"] = 1
trendweight["Computers"] = 1

def initializeDB():
    client = MongoClient()
    db = client.test
    print (db.list_collection_names())
    collection = db.CJOffers
    posts = db.posts
def sortSecond(val):
    a = list(val)
    return a[1]

def trend_weight(list):
    i = 0
    for each in list:
        if i ==3:
            break
        trendweight[each[0]] += each[1]
        i += 1

def trend_scrambller():
    for key in trendweight.keys():
        scrambler = random.random()*0.2-0.1
        trendweight[key] = trendweight[key]*(1+scrambler)

def parse_trend(trends):
    return None

def hard_work():
    f = open("categorized_clean.json", "r")
    Offerdata = f.readlines()
    f.close()
    f2 = open("categorized_clean2.json", "w")
    for each in Offerdata:
        f2.write(str(each)+","+"\n")
    f2.close()


def function_a(text):
    # this is the real deal
    scores = categorize(text)
    f = open("categorized_clean2.json", "r")
    OfferData = json.load(f)
    similarity = []
    ##############Get Trend
    ##############Parse Trend
    ############## Trend weight

    for each in OfferData["products"]:
        score = 0
        if list(scores[0])[0] == each['categoryName1']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * 1 * weight
        if list(scores[1])[0] == each['categoryName1']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * 1* weight
        if list(scores[2])[0] == each['categoryName1']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * 1* weight
        if list(scores[0])[0] == each['categoryName2']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * 0.7* weight
        if list(scores[1])[0] == each['categoryName2']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * 0.7* weight
        if list(scores[2])[0] == each['categoryName2']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * 0.7* weight
        if list(scores[0])[0] == each['categoryName3']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * 0.55* weight
        if list(scores[1])[0] == each['categoryName3']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * 0.55* weight
        if list(scores[2])[0] == each['categoryName3']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * 0.55* weight
        similarity.append([each, score])
    similarity.sort(key=sortSecond, reverse=True)
    chosen =[]
    for i in range(0,250):
        chosen.append(similarity[i*20])
    return chosen



def funuction_b():
    new_dict = {}
    new_dict["products"] = []
    f = open("capstone_all_with_pics_clean.json", "r")
    OfferData = json.load(f)
    i = 0
    for OneLine in OfferData["products"]:
        if i < 4000:
            i += 1
            continue
        if i >= 6000:
            break
        text = OneLine['title'] + " " + OneLine['title'] + " " + OneLine['title'] + " " + OneLine['description']
        new = text.encode('utf-8')
        cleanString = re.sub('\W+', ' ', new)
        response = requests.post('https://api.uclassify.com/v1/uclassify/Topics/classify', \
                                 data="{\"texts\": [\"%s\"]}" % (cleanString), \
                                 headers={'Authorization': 'Token ' + "QFlcgwbjS2P9"})
        response = response.json()
        responseCat = response[0]['classification']
        scores = []
        for each in responseCat:
            if each['className'] == 'Science':
                each['className'] = 'Technology'
            if each['className'] == 'Arts':
                each['className'] = 'Fashion'

            scores.append(each.values())
        scores.sort(key=sortSecond, reverse=True)
        # del OneLine["categoryName"]
        OneLine["categoryName1"] = str(scores[0][0])
        OneLine["categoryName2"] = str(scores[1][0])
        OneLine["categoryName3"] = str(scores[2][0])
        i += 1
        new_dict["products"].append(OneLine)
    new_dict2 = json.dumps(new_dict)
    with open("capstone_all_with_pics_clean4000-5100.json", "a+") as f:
        f.write(str(new_dict2))
    f.close()


def function_c(text):
    #this function is a local demonstration
    scores = categorize(text)
    f =open("local.json","r")
    OfferData = json.load(f)
    similarity=[]
    for each in OfferData:
        score = 0
        if list(scores[0])[0] == each['categoryname']:
            score += list(scores[0])[1]*1
        if list(scores[1])[0] == each['categoryname']:
            score += list(scores[1])[1] * 0.8
        if list(scores[2])[0] == each['categoryname']:
            score += list(scores[2])[1] * 0.6
        similarity.append([each,score])
    similarity.sort(key=sortSecond,reverse=True)
    chosen =[]
    for i in range(0,250):
        chosen.append(similarity[i*20])
    return chosen



def categorize(text):
    #################
    #tag selection rule:
    #select 3 tags with highests scores

    response = requests.post('https://api.uclassify.com/v1/uclassify/Topics/classify', \
                             data="{\"texts\": [\"%s\"]}" % (text), \
                             headers={'Authorization': 'Token ' + "QFlcgwbjS2P9"})
    response = response.json()
    responseCat = response[0]['classification']
    scores = []
    for each in responseCat:
        if each['className'] == 'Science':
            each['className'] = 'Technology'
        if each['className'] == 'Arts':
            each['className'] = 'Fashion'

        scores.append(each.values())
    scores.sort(key=sortSecond, reverse=True)
    return scores

if __name__ == "__main__":
    string ="sdf {} sdd".format("\"qee\"")
    #hard_work()
    # print  (string)
    trend_scrambller()
    readTech = "Many extremely helpful metrics and analytics have been developed to provide instrumentation for this journey: LTV (lifetime value of a customer), CAC (customer acquisition cost), Magic Number and SaaS  \
Quick Ratio are all very valuable tools. But the challenge in using derived metrics such as these is that there are often many assumptions, simplifications and sampling choices that need to go into these calculations, thus leaving the door open to skewed results.For example, \
when your company has only been selling for a year or two, it is extremely hard to know your true lifetime customer value. For starters, how do you know the right length of a “lifetime?”Taking one divided by your annual dollar \
churn rate is quite imperfect, especially if all or most of your customers have not yet reached their first renewal decision. How much account expansion is reasonable to assume if you only have limited evidence?\
LTV is most helpful if based on gross margin, not revenue, but gross margins are often skewed initially. When there are only a few customers to service, cost of goods sold (COGS) can appear artificially low because the true costs to serve have not yet been tracked as distinct cost centers as most of your team members wear multiple hats and pitch in ad hoc.\
Likewise, metrics derived from sales and marketing costs, such as CAC and Magic Number, can also require many subjective assumptions. When it’s just founders selling, how much of their time and overhead do you put into sales costs? Did you include all sales-related travel, event marketing and PR costs? I can’t tell you the number of times entrepreneurs have touted having a near-zero CAC when they are \
just starting out and have only handfuls of customers — which were mostly sold by the founder or are “friendly” relationships\
Even if you think you have nearly zero CAC today, you should expect dramatically rising sales costs once professional sellers, marketers, managers, and programs are put in place as you scale.\
One alternative to using derived metrics is to examine raw data, which is less prone to assumptions and subjectivity. The problem is how to do this efficiently and without losing the forest for the trees. The best tool I have encountered for measuring sales efficiency is called the 4×2 (that’s “four by two”) which I credit to Steve Walske, one of the master strategists of software sales, and the former CEO of PTC, a company renowned for its sales effectiveness and sales culture. [Here’s a podcast I did with Steve on How to Build a Sales Team.]\
The 4×2 is a color-coded chart where each row is an individual seller on your team and the columns are their quarterly performance shown as dollars sold. [See a 4×2 chart example below].\
Sales are usually measured as net new ARR, which includes new accounts and existing account expansions net of contraction, but you can also use new TCV (total contract value), depending on which number your team most focuses. In addition to sales dollars, the percentage of quarterly quota attainment is shown. The name 4×2 comes from the time frame shown: trailing four quarters, the current quarter, and the next quarter.\
Color-coding the cells turns this tool from a dense table of numbers into a powerful data visualization. Thresholds for the heatmap can be determined according to your own needs and culture. For example, green can be 80% of quota attainment or above, yellow can be 60% to 79% of quota, and red can be anything below 60%.\
Examining individual seller performance in every board meeting or deck is a terrific way to quickly answer many important questions, especially early on as you try to figure out your true position on the Sales Learning Curve. Publishing such leaderboards for your Board to see also tends to motivate your sales people, who are usually highly competitive and appreciate public recognition for a job well done, and likewise loathe to fall short of their targets in a public setting.\
"
    readHome = "First things first, THANK YOU! You guys shared soooo much love on my IGTV TOUR OF THE HOUSE , it made me feel so good about everything going on inside and out!! We are getting sooo, so close to finishing up our home and all of us could not be more excited. I’ve been sharing all sorts of project updates on my IG, but I want to take a beat and introduce you to some of the awesome sources we have used along the way. We’ve been lucky enough to work with some of my favorite brands to bring this beauty to life and I wanted to break it all down. Grab your notebook and take notes on all the things below!! WINDOWS & DOORS // When it came to ordering my windows and doors, I knew I wanted something that was beautiful yes, but also durable, timeless, and within budget. I have used MARVIN on a couple projects in the past, (see one example HERE) and it is one of my favorite window companies out there. When it came time to pull the trigger on which windows and doors I was going to use, MARVIN was a no brainer. I wrote an entire article about ALL MY SELECTIONS AND WHY I chose them — and now that you guys are starting to see the final product, it’s obvious why. Check out my previous post for allll the deets. PLUMBING // We used my forever favorite, WATERWORKS, for plumbing in the entire home. Once everything is installed and we’re a weee bit further along, I’ll do a room-by-room breakdown and link out to which collections and finishes I chose. Haaaang tight! EXTERIOR // I wanted to do a stacked stone, and searched high and low for the perfect vibe. I stumbled on some amazing images and sleuthed hard to find out that everything I was loving came from my friends over at HORIZON STONE. I am so beyond happy with how the exterior turned out, and for everyone asking, I chose from Horizon Stone’s ‘19TH CENTURY‘ series in the color ‘Hermitage.’ I used a custom blended grout, that my stone guys literally mixed on the spot, so don’t have a link out. HORIZON is very helpful however, and can point you in the right direction! We’re also painting a lot of the exterior, but I’m still deciding on my final, final color. Stay tuned for that!!! FLOORS // For most of the home, I chose the most beautiful white oak floors from my pals over at DUCHATEAU. I decided on the Varacio Collection in Tonale, which has random-width flooring… and I am just obsessed. We also worked with MISSION TILE for bricks, EXQUISITE SURFACES for my master bathroom stone floors, And CLE’ tile for every bathroom and my kitchen. And speaking of tile, we’re working with FIRECLAY for all of our pool tile (I can’t wait for you guys to see more of this!!). Check back here in a few weeks for a detailed outline of all the materials I chose! CEILING // Our friends at ROSS ALAN RECLAIMED provided the stuuuuning reclaimed white oak lumber in the ceiling that you all keep asking about. More to come about this also! CLOSETS // We’re using CONTAINER STORE CUSTOM CLOSETS for both my closets, Mike’s closet, and G’s closet. G and I have the “LAREN MODEL” and Mike has the “AVERA MODEL.” We’re also putting the “ELFA MODEL” in the guest room, office, and linen closets. It was so easy to go through the design consultation for the closets, and the install is happening in the next few weeks…I can hardly wait! INTERIOR PAINT // We worked with PORTOLA PAINTS for almost all of the interior paint of the house, and we will be sharing allll of the room by room deets soon, cause we know you guys will want to know!! GARAGE DOORS // I shared a peek at our custom garage doors on my IG a bit ago, and it seems like you’re all as obsessed as I am. We used reclaimed wood for the doors and they were custom built by CROWN DOORS & GATES (I couldn’t recommend them enough!) KITCHEN APPLIANCES // We have so many exciting appliances in the house, but the one I really can’t stop staring at is our LACANCHE RANGE. It’s the SULLY MODEL in black, and it’s gorge. Thats all for now, check my IG for updates on the house and when I will be posting more info about it all! Ps.. If you missed, the video tour, here it is!! ↓"
    list = function_a(readHome)
    for i in range (0,20):
        print (list[i])