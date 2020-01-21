import boto3
import json
import pymongo
import synonym.py

class key_score(object):

    def __init__(self, score, keyword):
        self.score = score
        self.keyword = keyword

    def __str__(self):
        return "score:%s, keyword:%s" % (self.score, self.keyword)


class offer(object):
    def __init__(self, text):
        self.text = text
        self.description = []
        self.title = []

    def addPairD(self, keysc):
        self.description.append(keysc)

    def addPairT(self, keysc):
        self.title.append(keysc)

    def getPairsD(self):
        return self.description

    def getPairsT(self):
        return self.title

    def getText(self):
        return self.text

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')


def function_a(text):
    returnNum = 0
    returnlist = []
    allOffers = Parse_Offer("capstone_shopping.json")
    keywordB = Parse_Blog(text)
    total_count = keywordB.__len__()
    good_count = 3
    valid_count = 0
    for x in allOffers:
        OfferText = x.getText()
        OfferKeywords = x.getPairsT()  # get the list of keywords stripped from the title
        for offerKeyword in OfferKeywords:  # check if a list of keywords from offer x matches text y
            for blogKeyword in keywordB:
                if synonym.check(offerKeyword,blogKeyword) > 0.6:
                    valid_count += 1
                if valid_count >= good_count:  # if enough words matched, break from loop
                    break
            if valid_count >= good_count:  # again, break from this loop too
                break
        returnlist.append(OfferText)
        returnNum += 1
        valid_count = 0
        if returnNum >= 10: # if 10 offers matched, finish the algorithm and return
            break
    return returnlist





def Parse_Offer(text):
    all_offer =[]
    #comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    with open(text, 'r') as load_f:
        OfferData = json.load(load_f)
        for x in OfferData['products']:
            text2 = x['title']  # + text['description']
            TheOffer = offer(x)
            print('Calling detectingkeywords')
            OutPutFAWS = comprehend.detect_key_phrases(Text=text2, LanguageCode='en')
            print('End of detectingkeywords')
            keyPhrases = OutPutFAWS['KeyPhrases']
            for segment in keyPhrases:
                keyword = segment['Text']
                Score = segment['Score']
                if (Score < 60):
                    continue;
                TheOffer.addPairT(keyword)
            all_offer.append(TheOffer)
    return all_offer

    # pair = key_score(Score, keyword)
    # newoffer.addPair(pair)
    # print  newoffer.getPairs()[0]
    # Offerlist.append(newoffer)
    # break

    ## this segment of loop test the functionality of printing the organized
    # keywords in an offer
    # print Offerlist[0].getText()
    # for x in Offerlist[0].getPairs():
    #   print x


def Parse_Blog(text):
    keywordlist = []
    #comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    # with open("capstone_shopping.json", 'r') as load_f:
    # OfferData = json.load(load_f)
    # for x in OfferData['products']:
    print('Calling detectingkeywords')
    OutPutFAWS = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
    print('End of detectingkeywords')
    keyPhrases = OutPutFAWS['KeyPhrases']
    for segment in keyPhrases:
        keyword = segment['Text']
        Score = segment['Score']
        if (Score < 60):
            continue;
        keywordlist.append(keyword)
    return keywordlist


if __name__ == "__main__":
    Parse_Offer("capstone_shopping.json")