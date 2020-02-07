# -*- coding: UTF-8 -*-
import requests
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import json
import re

def initializeDB():
    client = MongoClient()
    db = client.test
    print (db.list_collection_names())
    collection = db.CJOffers
    posts = db.posts
def sortSecond(val):
    a = list(val)
    return a[1]

def function_a(text):
    scores = categorize(text)



def funuction_b():
    #this function categorizes every offers on the database
    new_dict ={}
    new_dict["products"] = []
    f =open("capstone_all_with_pics_clean.json","r")
    OfferData = json.load(f)
    i =0
    for OneLine in OfferData["products"]:
        if i < 4000:
            i += 1
            continue
        if i >= 6000:
            break
        text =OneLine['title']+" "+OneLine['title']+" "+OneLine['title']+" "+OneLine['description']
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
        #del OneLine["categoryName"]
        OneLine["categoryName1"] = str(scores[0][0])
        OneLine["categoryName2"] = str(scores[1][0])
        OneLine["categoryName3"] = str(scores[2][0])
        i +=1
        new_dict["products"].append(OneLine)
    new_dict2= json.dumps(new_dict)
    with open("capstone_all_with_pics_clean4000-5100.json", "a+") as f:
        f.write(str(new_dict2))
        f.close()
    return None


def function_c(text):
    #this function is a local demonstration
    scores = categorize(text)
    f =open("capstone_all_with_pics_clean3.json","r")
    OfferData = json.load(f)
    similarity=[]
    for each in OfferData['products']:
        score = 0
        if list(scores[0])[0] == each['categoryname']:
            score += list(scores[0])[1]*1
        if list(scores[1])[0] == each['categoryname']:
            score += list(scores[1])[1] * 0.8
        if list(scores[2])[0] == each['categoryname']:
            score += list(scores[2])[1] * 0.6
        similarity.append([each,score])
    similarity.sort(key=sortSecond,reverse=True)
    similarity= json.dumps(similarity)
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
    print  (string)
    funuction_b()
    #print (function_c("The car/van picks you up from Noi Bai airport (in Ha Noi) to take you to the heart of the city. After arriving at the hotel after a 40-minute drive, check in and have a free time to walk around Old Quarter or explore the night market in Ha Noi downtown.Until 21:00 pm: Our guide will pick up you at your hotel for boarding the train to travel to Lao Cai."))