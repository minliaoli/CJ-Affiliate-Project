# -*- coding: UTF-8 -*-
import requests
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import json


def initializeDB():
    client = MongoClient()
    db = client.test
    print (db.list_collection_names())
    collection = db.CJOffers
    posts = db.posts
def sortSecond(val):
    return val[1]

def function_a(text):
    scores = categorize(text)



def funuction_b():
    #this function categorizes every offers on the database
    return None


def function_c(text):
    #this function is a local demonstration
    scores = categorize(text)
    f =open("local.json","r")
    OfferData = json.load(f)
    similarity=[]
    for each in OfferData:
        score = 0
        if scores[0][0] == each['categoryname']:
            score += scores[0][1]*1
        if scores[1][0] == each['categoryname']:
            score += scores[0][1] * 0.8
        if scores[2][0] == each['categoryname']:
            score += scores[0][1] * 0.6
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
    print (string)
    print (function_c("The car/van picks you up from Noi Bai airport (in Ha Noi) to take you to the heart of the city. After arriving at the hotel after a 40-minute drive, check in and have a free time to walk around Old Quarter or explore the night market in Ha Noi downtown.Until 21:00 pm: Our guide will pick up you at your hotel for boarding the train to travel to Lao Cai."))