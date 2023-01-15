import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


if __name__ == '__main__':

    inp=input("Give me your txt file\n")
    f=open(inp+'.txt','r+')

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(f)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)

    print(df.transpose())

    indexes=list(df.transpose().index)
    data=pd.DataFrame(cosine_similarity(df.transpose()))
    data.index=indexes[:]
    data.columns=indexes[:]

    print(data)