import boto3
import json

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


def Parse_Offer(filename):
    Offerlist = []
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    with open(filename, 'r') as load_f:
        OfferData = json.load(load_f)
        for x in OfferData['products']:
            textTitle = x['title']
            textDescription = x['description']
            print('Calling detectingkeywords')
            OutPutFAWS = comprehend.detect_key_phrases(Text=textTitle, LanguageCode='en')
            OutPutFAWS2 = comprehend.detect_key_phrases(Text=textDescription, LanguageCode='en')
            print('End of detectingkeywords')
            newoffer = offer(x)
            keyPhrases = OutPutFAWS['KeyPhrases']
            #print keyPhrases
            for segment in keyPhrases:
                keyword = segment['Text']
                Score = segment['Score']
                keyword.encode("ascii")
                pair = key_score(Score, keyword)
                newoffer.addPairT(pair)
                #print  newoffer.getPairs()[0]
            keyPhrases = OutPutFAWS2['KeyPhrases']
            for segment in keyPhrases:
                keyword = segment['Text']
                Score = segment['Score']
                pair = key_score(Score, keyword)
                newoffer.addPairD(pair)
            Offerlist.append(newoffer)
            break

    ## this segment of loop test the functionality of printing the organized
    # keywords in an offer
    print Offerlist[0].getText()
    print 'TITLE'
    for x in Offerlist[0].getPairsT():
        print x
    print 'Description'
    for x in Offerlist[0].getPairsD():
        print x
    ##########detecting entities
    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=textDescription, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')

####there are lots of redundencies in offers, maybe we can clean them
def Clean_Offers():
    with open("capstone_all.json", 'r') as load_f:
        OfferData = json.load(load_f)




if __name__ == "__main__":
    Parse_Offer("capstone_shopping.json")


