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
        self.key_scores = []

    def addPair(self, keysc):
        self.key_scores.append(keysc)

    def getPairs(self):
        return self.key_scores

    def getText(self):
        return self.text


def Parse_Offer():
    Offerlist = []
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    with open("capstone_shopping.json", 'r') as load_f:
        OfferData = json.load(load_f)
        for x in OfferData['products']:
            text = x['title'] + x['description']
            print('Calling detectingkeywords')
            OutPutFAWS = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
            print('End of detectingkeywords')
            newoffer = offer(x)
            keyPhrases = OutPutFAWS['KeyPhrases']
            #print keyPhrases
            for segment in keyPhrases:
                keyword = segment['Text']
                Score = segment['Score']
                pair = key_score(Score, keyword)
                newoffer.addPair(pair)
                #print  newoffer.getPairs()[0]
            Offerlist.append(newoffer)
            break

    ## this segment of loop test the functionality of printing the organized
    # keywords in an offer
    print Offerlist[0].getText()
    for x in Offerlist[0].getPairs():
        print x




##########detecting entities
    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')

if __name__ == "__main__":
    Parse_Offer()
    """
    You can use this to test your code.
    python hw2.py [training file path] [testing file path]
    """

