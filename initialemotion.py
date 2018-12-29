import pandas
import random
from subprocess import call
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions, KeywordsOptions, EmotionOptions, EntitiesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='Emup9q41iwB7B_jsKVoc3vRjD1RFwS_GnWorTGkj3opd',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

data = pandas.read_csv('lyrics/emotion_lyrics.csv')

start_index = 4000
sadness = []
joy = []
fear = []
disgust = []
anger = []
keywords = []

for i in range(start_index):
    sadness.append(data['sadness'][i])
    joy.append(data['joy'][i])
    fear.append(data['fear'][i])
    disgust.append(data['disgust'][i])
    anger.append(data['anger'][i])
    keywords.append(data['keywords'][i])

for i in range(862):
    print(i)
    response = natural_language_understanding.analyze(
        language = 'en',
        text = data['lyric'][i+start_index],
        features=Features(
            keywords=KeywordsOptions(sentiment=False, emotion=False, limit=1),
            emotion=EmotionOptions()
        )).get_result()
    #data['sadness'] = [None] * len(data['lyric'])
    #print(data['sadness'])

    sadness.append(response['emotion']['document']['emotion']['sadness'])
    joy.append(response['emotion']['document']['emotion']['joy'])
    fear.append(response['emotion']['document']['emotion']['fear'])
    disgust.append(response['emotion']['document']['emotion']['disgust'])
    anger.append(response['emotion']['document']['emotion']['anger'])

    if len(response['keywords']) > 0:
        keywords.append(response['keywords'][0]['text'])
    else:
        keywords.append(None)
    #data.loc[:, ('sadness', i)] = response['emotion']['document']['emotion']['sadness']
    #data['sadness'].append("test") 

for i in range( len(data['lyric']) - len(sadness) ):
    sadness.append(None)
    joy.append(None)
    fear.append(None)
    disgust.append(None)
    anger.append(None)
    keywords.append(None)

data['keywords'] = keywords

data['sadness'] = sadness
data['joy'] = joy
data['fear'] = fear
data['disgust'] = disgust
data['anger'] = anger

data.to_csv('lyrics/emotion_lyrics.csv')

#print(json.dumps(response, indent=2))

