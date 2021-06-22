import pandas
import json
import sys
import os
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions, EmotionOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey=os.environ["APIKEY"],
    url=os.environ["APIURL"]
)

data = pandas.read_csv('lyrics/emotion_lyrics.csv')

text_to_translate = "caitlin studies alot"

response = natural_language_understanding.analyze(
        language = 'en',
        text = text_to_translate,
        features=Features(
            keywords=KeywordsOptions(sentiment=False, emotion=False, limit=2),
            emotion=EmotionOptions()
        )).get_result()

lowest_diff = 1
emotion_lyric = ""
keyword_lyric = ""
keyword_diff = 1
for i in range(len(data['lyric'])):
    sum_diff = 0
    for emotion in ['sadness', 'joy', 'fear', 'disgust', 'anger']:
        diff = response['emotion']['document']['emotion'][emotion] - data[emotion][i]
        diff = diff**2
        sum_diff += diff
    if sum_diff < lowest_diff:
        lowest_diff = sum_diff
        emotion_lyric = data['lyric'][i]
        #print(str(sum_diff) + " || " + data['lyric'][i])
        #if response['keywords'][0]['text'] == data['keywords'][i]:
            #print("OOOH BABEE")
    #if response['keywords'][0]['text'] == data['keywords'][i]:
    #    if sum_diff < keyword_diff:
    #        keyword_diff = sum_diff
    #        keyword_lyric = data['lyric'][i]
        #print("keyword match || " + data['lyric'][i])

print("emotion: " + emotion_lyric)
print("keyword: " + keyword_lyric)
#print(json.dumps(response, indent=2))
print(response['keywords'][0]['text'])
print(response['emotion']['document']['emotion'])
