# neural networks
from tensorflow import keras
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

# text processing
import csv
import json
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from functions import *

# graphs
import matplotlib.pyplot as plt 
import seaborn as sns

# maths
import pandas as pd
import numpy as np

# others
import os
import joblib
from tqdm import tqdm

model=joblib.load('model.joblib')
multilabel_binarizer=joblib.load('multilabel_binarizer.joblib') 
tfidf_vectorizer=joblib.load('tfidf_vectorizer.joblib') 
decode_genres=joblib.load('decode_genres.joblib') 

def infer_genres(text
                 ,model=model
                 ,binarizer=multilabel_binarizer
                 ,vectorizer=tfidf_vectorizer
                 ,decoder=decode_genres
                ):
    text = clean_text(text)
    text = remove_stopwords(text)
    q_vec = vectorizer.transform([text])
    q_pred = model.predict(q_vec)
    genres = binarizer.inverse_transform(q_pred)
    genres = [decoder[item] for t in genres for item in t]
    return genres

if __name__ == "__main__":
    print(infer_genres("this is the plot of a romantic comedy movie"))
    print(infer_genres("this is the plot of an action movie"))
