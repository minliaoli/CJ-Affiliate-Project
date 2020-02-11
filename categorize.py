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
            score += list(scores[0])[1] * 0.8* weight
        if list(scores[1])[0] == each['categoryName2']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * 0.8* weight
        if list(scores[2])[0] == each['categoryName2']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * 0.8* weight
        if list(scores[0])[0] == each['categoryName3']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * 0.6* weight
        if list(scores[1])[0] == each['categoryName3']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * 0.6* weight
        if list(scores[2])[0] == each['categoryName3']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * 0.6* weight
        similarity.append([each, score])
    similarity.sort(key=sortSecond, reverse=True)
    return similarity



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
    return similarity



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
    list = function_a(" ought to be talking about Verona. We ought to be talking about an astonishing week for the club with the lowest wage bill in Serie A, in which they drew with Milan and Lazio before beating the champions, and league leaders, Juventus. We ought to be talking about how a newly promoted side went from battling relegation to sixth place, via an eight-game unbeaten run, inspired by a manager with a passion for death metal.")
    for i in range (0,20):
        print (list[i])