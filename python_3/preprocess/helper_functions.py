# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:35:51 2021
function to check missing data
input parameter: dataframe
output: missing data values
@author: Ashish
"""
# import required libraries
import re, os, emoji, numpy as np
import pandas as pd
#Count vectorizer for N grams
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

# Nltk for tekenize and stopwords
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


def find_missing_data_vals(data):
    total=data.isnull().sum().sort_values(ascending=False)
    percentage=round(total/data.shape[0]*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

def categorical_value_counts(data,feature):
    total=data.loc[:,feature].value_counts(dropna=False)
    percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

def find_unique_values_in_column(data,feature):
    unique_val=pd.Series(data.loc[:,feature].unique())
    return pd.concat([unique_val],axis=1,keys=['Unique Values'])

def find_duplicate_data_vals(data):
    dup=[]
    columns=data.columns
    for i in data.columns:
        dup.append(sum(data[i].duplicated()))
    return pd.concat([pd.Series(columns),pd.Series(dup)],axis=1,keys=['Columns','Duplicate count'])

# # regualr expression based helper functions
# re.findall - Module is used to search for “all” occurrences that match a given pattern.
# re.sub - Substitute the matched RE patter with given text
# re.match - The match function is used to match the RE pattern to string with optional flags
# re.search - This method takes a regular expression pattern and a string and searches for that pattern with the string.

def find_url_in_text(string): 
    text = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return "".join(text) # converting return value from list to string

def find_emoji_in_text(text):
    emo_text=emoji.demojize(text)
    line=re.findall(r'\:(.*?)\:',emo_text)
    return line

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def find_email_in_text(text):
    line = re.findall(r'[\w\.-]+@[\w\.-]+',str(text))
    return ",".join(line)

def find_hash_in_text(text):
    line=re.findall(r'(?<=#)\w+',text)
    return " ".join(line)

def find_at_in_text(text):
    line=re.findall(r'(?<=@)\w+',text)
    return " ".join(line)

def find_number_in_text(text):
    line=re.findall(r'[0-9]+',text)
    return " ".join(line)

def find_phone_number_in_text(text):
    line=re.findall(r"\b\d{10}\b",text)
    return "".join(line)

# find years between 1900-2021
def find_year_in_text(text):
    line=re.findall(r"\b(19[00][0-9]|20[0-1][0-9]|2021)\b",text)
    return line

def find_punct_in_text(text):
    line = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string="".join(line)
    return list(string)

def stop_word_in_text(text):
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(text) 
    non_stop_words = [w for w in word_tokens if not w in stop_words] 
    stop_words= [w for w in word_tokens if w in stop_words] 
    return stop_words

def find_nonalp_in_text(text):
    line = re.findall("[^A-Za-z0-9 ]",text)
    return line

def find_top_ngrams_in_text(corpus,ngram_range,n=None):
    """
    List the top n words in a vocabulary according to occurrence in a text corpus.
    """
    vec = CountVectorizer(stop_words = 'english',ngram_range=ngram_range).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    total_list=words_freq[:n]
    df=pd.DataFrame(total_list,columns=['text','count'])
    return df

def find_only_words_in_text(text):
    line=re.findall(r'\b[^\d\W]+\b', text)
    return " ".join(line)

def only_numbers_in_text(text):
    line=re.findall(r'\b\d+\b', text)
    return " ".join(line)

def pick_unique_sentence(text):
    line=re.findall(r'(?sm)(^[^\r\n]+$)(?!.*^\1$)', text)
    return line

def find_capital(text):
    line=re.findall(r'\b[A-Z]\w+', text)
    return line

def remove_html_tag(string):
    text=re.sub('<.*?>','',string)
    return text

def find_ip_address(string):
    text=re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',string)
    return text

def find_lat_lon(string):
    text=re.findall(r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$',string)
    if text!=[]:
        print("[{}] is valid latitude & longitude".format(string))
    else:
        print("[{}] is not a valid latitude & longitude".format(string))

