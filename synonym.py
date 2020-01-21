from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def check(keywordO,keywordB):
    lemmatizer = WordNetLemmatizer()
    g = lemmatizer.lemmatize('Cardigan',pos='v')
    print (g)
    w1 = wordnet.synset('Cardigan.n.01')
    w2 = wordnet.synset('car.n.01')
    print(w1.wup_similarity(w2))
    # for O in keywordO:
    #     for B in keywordB:
    #         word=O+'.n.01'
    #         word2=B+'.n.01'
    #         prep = wordnet.synset(word2)
    #         prep2 = wordnet.synset(word)
    #         print(prep.wup_similarity(prep2))

