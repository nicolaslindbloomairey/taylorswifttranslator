import pandas
import random
from subprocess import call

data = pandas.read_csv('lyrics/all_lyrics.csv')

i = random.randint(0, len(data['lyric']))
for j in range(3):
    print(data['lyric'][i+j])
    call(["say", "-v", "Samantha", data['lyric'][i+j]])

print("\nFrom " + data['track_title'][i] + " - " + data['album'][i] + ", line number " + str(data['line'][i]))
