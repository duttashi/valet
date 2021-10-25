# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:35:51 2021
function to check missing data
input parameter: dataframe
output: missing data values
@author: Ashish
"""

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

