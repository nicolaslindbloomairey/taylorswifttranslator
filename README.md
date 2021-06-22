# taylorswifttranslator

Uses IBM watson natural language processing to translate any user-given phrase to a lyric written by Taylor Swift based on how emotionally similar the phrase is to all taylor swift lyrics.

Usage:
```
$ python3 translate.py "text to translate"
```

How it works:
Behind the scenes we first pass every lyric written by taylor swift into the natural language processing API which returns to us a 6-dimensional vector with values 0-1 representing how much that emotion is present in the phrase. Then we do the same with the user provided phrase and then we return the closest taylor swift lyric with repect to the 6-dimensional euclidean distance metric.

Possible improvements?
  - context for both the lyrics and the provided phrase
  - better metric?

All the lyrics are trademarked by taylor swift.
