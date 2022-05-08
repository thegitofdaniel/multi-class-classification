###############################################
##### Packages ################################
###############################################

import re
from nltk.corpus import stopwords
from nltk import FreqDist
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###############################################
##### Text Processing #########################
###############################################

def clean_text(text):
    # remove backslash-apostrophe 
    text = re.sub("\'", "", text) 
    # remove everything except alphabets 
    text = re.sub("[^a-zA-Z]"," ",text) 
    # remove whitespaces 
    text = ' '.join(text.split()) 
    # convert text to lowercase 
    text = text.lower() 
    return text

stop_words = set(stopwords.words('english'))
def remove_stopwords(text, stop_words=stop_words):
    no_stopword_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopword_text)

def full_text_clean(text, stop_words=stop_words):
    text = clean_text(text)
    text = remove_stopwords(text, stop_words)
    return text

def freq_words(x
               ,terms = 30
               ,title="Most Frequent Words"
               ,largest=True
               ,color="blue"
              ):
    
    """
    x can be:
    - a pandas dataframe with a list of strings
    - a long string
    - an nltk FreqDist object
    
    """
    if type(x)==pd.DataFrame:
        all_words = ' '.join([text for text in x])
        all_words = all_words.split() 
        fdist = FreqDist(all_words)
    elif type(x)==str:
        all_words = x.split() 
        fdist = FreqDist(all_words)
    elif type(x)==FreqDist:
        fdist = x
    else:
        pass
        
    words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())}) 
    
    # select the n most frequent words
    if largest == True:
        d = words_df.nlargest(columns="count", n = terms)
    else:
        d = words_df.nsmallest(columns="count", n = terms)
    
    # visualize words and frequencies
    plt.figure(figsize=(12,18))
    ax = sns.barplot(data=d
                     ,x="count"
                     ,y="word"
                     ,color=color
                    )
    ax.set(ylabel = 'word')
    plt.title(title,fontsize=18)
    plt.show()