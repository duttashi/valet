# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:12:21 2021
custom functions for feature encoding
@author: Ashish
"""
from sklearn.preprocessing import  OrdinalEncoder, LabelEncoder, OneHotEncoder
# label encoding
def label_encoding(feature):
    le = LabelEncoder()
    #le.fit(train_df[feature].unique().tolist() + test_df[feature].unique().tolist())
    df[f"{feature}_le"] = le.transform(df[feature])
    #test_df[f"{feature}_le"] = le.transform(test_df[feature])
    return f"{feature}_le"

# leave one out encoding
def loo_encoding(feature):
    loo = LeaveOneOutEncoder()
    loo.fit(train_df[feature], train_df["target"])
    train_df[f"{feature}_loo"] = loo.transform(train_df[feature])
    test_df[f"{feature}_loo"] = loo.transform(test_df[feature])
    return f"{feature}_loo"

# one hot encoding
def oh_encoding(feature):
    oh = OneHotEncoder(sparse=False)
    oh.fit(train_df[feature].unique().tolist() + test_df[feature].unique().tolist())
    new_features = [f"{feature}_{item}" for item in oh.categories_[0]]
    train_df[new_features] = oh.transform(train_df[feature])
    test_df[new_features] = oh.transform(test_df[feature])
    return new_features
    





