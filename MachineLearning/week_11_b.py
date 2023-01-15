from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
import pandas as pd
warnings.filterwarnings(action = 'ignore')

if __name__ == '__main__':
    inp = input("Give me your txt file\n")
    f = open(inp + '.txt', 'r+')
    s = f.read()
    filereader = s.replace("\n", " ")
    data = []

    for sentence in sent_tokenize(filereader):
        temp = []
        for word in word_tokenize(sentence):
            temp.append(word.lower())
        data.append(temp)

    model = gensim.models.Word2Vec(data, min_count = 1, window = 5)

    dict={}
    for i in sent_tokenize(filereader):
        for j in word_tokenize(i):
            if j.isalpha()==True:
                dict[j]=model.wv.most_similar(j.lower(),topn=60)
                #print("{}->".format(j.lower),model.wv.most_similar(j.lower()))

    #print(dict)
    print(pd.DataFrame.from_dict(dict).transpose())
