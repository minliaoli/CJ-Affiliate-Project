# -*- coding: UTF-8 -*-
import requests
import pymongo
from pymongo import MongoClient
import datetime
import pprint
import json
import random
import xmltodict
import io
# import urllib2
# from bs4 import BeautifulSoup
# import re
import trendy
import math
import re

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
STEP = 20
STEP_function_d = 5
STEPRandomness = 0  # defines how variated the steps will be.
FIRST = 1
SECOND = 0.8
THIRD = 0.55
trendMaxDis= 0.8  #defines the maximum any trendweight can be pushed


def sortSecond(val):
    a = list(val)
    return a[1]

def trend_weight(list):
    i = 0
    for each in list:
        if i ==10:
            break
        trendweight[each[0]] += each[1]
        i += 1

def trend_scrambller():
    for key in trendweight.keys():
        scrambler = random.random()*0.2-0.1
        trendweight[key] = trendweight[key]*(1+scrambler)

def parse_trend(trends):
    trendweight2 = {}
    trendweight2["Fashion"] = 0
    trendweight2["Recreation"] = 0
    trendweight2["Sports"] = 0
    trendweight2["Games"] = 0
    trendweight2["Health"] = 0
    trendweight2["Home"] = 0
    trendweight2["Business"] = 0
    trendweight2["Technology"] = 0
    trendweight2["Society"] = 0
    trendweight2["Computers"] = 0

    for each in trends:
        text = each[0]+" "
        text = text*10
        scores = categorize(text)
        for eachCat in scores:
            trendweight2[list(eachCat)[0]] += list(eachCat)[1]*each[1]
    for eachone in trendweight2:
        trendweight[eachone] += trendweight2[eachone]/10  ##this defines the scope of which we apply onto real trends
    return trendweight

def reset_trend():
    trendweight["Fashion"] = 1
    trendweight["Recreation"] = 1
    trendweight["Sports"] = 1
    trendweight["Games"] = 1
    trendweight["Health"] = 1
    trendweight["Home"] = 1
    trendweight["Business"] = 1
    trendweight["Technology"] = 1
    trendweight["Society"] = 1
    trendweight["Computers"] = 1

def store_trendWeight(weight):
    with open("trendweight.txt","w+") as f:
        for each in weight:
            f.write(each+","+str(weight[each])+"\n")

def load_weight():
    with open("trendweight.txt","r+") as f:
        data = f.readlines()
        for each in data:
            each = each.split(",")
            each[1] = float(each[1])
            trendweight[each[0]]=each[1]

def return_current_trendweight():
    load_weight()
    data={}
    for each in trendweight:
        data[each]=trendweight[each]
    reset_trend()
    return data

def return_pop_keywords():
    data = trendy.get_trends()
    result=[]
    for smallList in data:
        p=re.sub("[^a-zA-Z0-9]+", " ", smallList[0])
        result.append(p)
    strResult=re.sub("[']+", '"', str(result))
    return str(strResult)

def hard_work():
    f = open("categorized_clean.json", "r")
    Offerdata = f.readlines()
    f.close()
    f2 = open("categorized_clean2.json", "w")
    for each in Offerdata:
        f2.write(str(each)+","+"\n")
    f2.close()

# this is the real deal
# U ==1 means the imput is an URL
# T==1 means to use trend
def function_a(text, U, T):
    reset_trend()
    if T ==1:
        load_weight()
    if U ==1:
        scores = categorizeUrl(text)
    else:
        scores = categorize(text)
    f = io.open("categorized_clean2.json", mode="r", encoding="utf-8")
    OfferData = json.load(f)
    similarity = []
    ##############Get Trend
    ##############Parse Trend
    ############## Trend weight
    trend_scrambller()
    for each in OfferData["products"]:
        score = 0
        if list(scores[0])[0] == each['categoryName1']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * FIRST * weight
        if list(scores[1])[0] == each['categoryName1']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * FIRST * weight
        if list(scores[2])[0] == each['categoryName1']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * FIRST * weight
        if list(scores[0])[0] == each['categoryName2']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * SECOND * weight
        if list(scores[1])[0] == each['categoryName2']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * SECOND * weight
        if list(scores[2])[0] == each['categoryName2']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * SECOND * weight
        if list(scores[0])[0] == each['categoryName3']:
            weight = trendweight[list(scores[0])[0]]
            score += list(scores[0])[1] * THIRD * weight
        if list(scores[1])[0] == each['categoryName3']:
            weight = trendweight[list(scores[1])[0]]
            score += list(scores[1])[1] * THIRD * weight
        if list(scores[2])[0] == each['categoryName3']:
            weight = trendweight[list(scores[2])[0]]
            score += list(scores[2])[1] * THIRD * weight
        similarity.append([each, score])
    similarity.sort(key=sortSecond, reverse=True)
    chosen =[]
    for i in range(20):
        chosen.append(similarity[i*STEP][0])  ######################STEP 20###########################
    chosen = json.dumps(chosen)
    return str(chosen)



def funuction_b():
    #parse all the offers
    new_dict = {}
    new_dict["products"] = []
    f = io.open("capstone_all.json", mode="r", encoding="utf-8")
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
        cleanString = new.sub('\W+', ' ', new)
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
    f = io.open("categorized_clean2.json", mode="r", encoding="utf-8")
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
        chosen.append(similarity[i*15])
    return chosen


def function_d(text,U):
    load_weight()
    if U ==1:
        scores = categorizeUrl(text)
    else:
        scores = categorize(text)
    f = io.open("categorized_clean2.json", mode="r", encoding="utf-8")
    OfferData = json.load(f)
    similarity = []
    for each in OfferData["products"]:
        score = trendweight[each['categoryName1']]*FIRST+\
                trendweight[each['categoryName2']]*SECOND+\
                trendweight[each['categoryName3']]*THIRD
        if list(scores[0])[0] == each['categoryName1']:
            score += list(scores[0])[1] * FIRST*0.5
        if list(scores[1])[0] == each['categoryName1']:
            score += list(scores[1])[1] * FIRST*0.5
        if list(scores[2])[0] == each['categoryName1']:
            score += list(scores[2])[1] * FIRST*0.5
        if list(scores[0])[0] == each['categoryName2']:
            score += list(scores[0])[1] * SECOND*0.5
        if list(scores[1])[0] == each['categoryName2']:
            score += list(scores[1])[1] * SECOND*0.5
        if list(scores[2])[0] == each['categoryName2']:
            score += list(scores[2])[1] * SECOND*0.5
        if list(scores[0])[0] == each['categoryName3']:
            score += list(scores[0])[1] * THIRD*0.5
        if list(scores[1])[0] == each['categoryName3']:
            score += list(scores[1])[1] * THIRD*0.5
        if list(scores[2])[0] == each['categoryName3']:
            score += list(scores[2])[1] * THIRD*0.5
        similarity.append([each, score])
    similarity.sort(key=sortSecond, reverse=True)
    chosen = []
    for i in range(5):
        chosen.append(similarity[i * STEP_function_d][0])  ######################STEP 5###########################
    chosen = json.dumps(chosen)
    return str(chosen)




def function_a2(text):
    ##try to use IABv2 standards
    #todo
    return None


def function_b2():
    #todo
    return None

def categorizeUrl(Url):
    response = requests.get("http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=QFlcgwbjS2P9&url={}&version=1.01".format(Url))
    response = response.text
    classification = xmltodict.parse(response)
    responseCat = classification['uclassify']['readCalls']['classify']['classification']['class']
    scores = []
    for each in responseCat:
        if each['@className'] == 'Science':
            each['@className'] = 'Technology'
        if each['@className'] == 'Arts':
            each['@className'] = 'Fashion'
        values =each.values()
        values = list(values)
        values[1] =float(values[1])
        scores.append(values)
    scores.sort(key=sortSecond, reverse=True)
    return scores


def categorize(text):
    #################
    #tag selection rule:
    #select 3 tags with highests scores
    #text=text.encode("ascii","ignore")
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
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


def generate_trend_weight_sheet():
    ## this will generate a locally parsed data for use in trending
    trends = trendy.get_trends()
    weights = parse_trend(trends)
    store_trendWeight(weights)


if __name__ == "__main__":
    # parse_trend(trendy.get_trends())
    # store_trendWeight(trendweight)
    urltest = "https://docs.python.org/2/library/csv.html"
    #categorizeUrl(urltest)
    listing = function_a(urltest,1,0)
    print(trend_weight)
    print (listing)
    list2 = function_d(urltest,1)
    print(list2)