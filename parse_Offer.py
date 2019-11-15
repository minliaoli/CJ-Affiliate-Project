import boto3
import json
if __name__ == "__main__":
    """
    You can use this to test your code.
    python hw2.py [training file path] [testing file path]
    """
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    text = "It is raining today in Seattle, I wonder what's gonna happen the day after this critical meeting"
##########detecting keywords
    print('Calling DetectKeyPhrases')
    print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectKeyPhrases\n')

##########detecting entities
    print('Calling DetectEntities')
    print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectEntities\n')