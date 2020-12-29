# Symptom Analyzer For Diagnose

![](https://i.ibb.co/s6yZqCC/Untitled.jpg)

## Project Members
Emre YAVUZ
Adem ÖZER


## Project Details
System make decisions about symptoms and diseases using NLP methods and user input. First, taken input from user sends to model that compare datas. System apply some NLP methods like stemming and tokenization. Stemmed and tokenized words are compares with dataset values. Exact matches increase possibility of right disease detection.

## Project Dependencies
```
import pandas as pd
import re
import glob,csv
from operator import is_not
from functools import partial
import json
from translate import Translator
from TurkishStemmer import TurkishStemmer
from polyglot.text import Text
import codecs
import nltk
from nltk.corpus import stopwords
import itertools
import operator
```

## Datasets
Dataset took at Kaggle and translated using Google Translate API.
`<link>` : <https://www.kaggle.com/plarmuseau/sdsort>
