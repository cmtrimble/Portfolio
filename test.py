import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import spacy
import requests
from transformers import pipeline
from bs4 import BeautifulSoup
import re
import unicodedata
from contractions import CONTRACTION_MAP
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.toktok import ToktokTokenizer
import language_tool_python as ltp
import sys
print(sys.executable)
