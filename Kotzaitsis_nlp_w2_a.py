import nltk
import ssl
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.util import pad_sequence,ngrams
from nltk.lm.preprocessing import pad_both_ends,padded_everygram_pipeline
from itertools import chain
from nltk.lm import MLE
from nltk.tokenize.treebank import TreebankWordDetokenizer
import random

def downloaddata(name):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download(str(name))
    nltk.download('punkt')
    return

def tokenization(rawText):
    sentences = sent_tokenize(rawText)
    wordsPerSentence=[word_tokenize(t) for t in sentences]
    words = word_tokenize(rawText)
    return words,wordsPerSentence,sentences

def Freq(list,fileName):
    f=open(str(fileName),'w+')
    Freq = nltk.FreqDist(list)
    for k, v in Freq.items():
        txt="{}, {}\n".format(k,v)
        f.write(txt)
    Freq.plot(10)

def bigramms(wordsPerSentence):
    bigrammsList=[]
    for i in wordsPerSentence:
        padding=list(pad_both_ends(i,n=2))
        bigramm=list(ngrams(padding,2))
        bigrammsList.append(bigramm)
    bigrammsList = list(chain.from_iterable(bigrammsList))
    Freq(bigrammsList,"bigramm.txt")


def trigramms(wordsPerSentence):
    trigrammList=[]
    for i in wordsPerSentence:
        padding=list(pad_sequence(pad_both_ends(i,n=2),pad_left=True,left_pad_symbol="<s>",n=2))
        trigramm=list(ngrams(padding,3))
        trigrammList.append(trigramm)
    trigrammList=list(chain.from_iterable(trigrammList))
    Freq(trigrammList,"trigramm.txt")

def trigrammsSentences(wordsPerSentence):
    train, vocab = padded_everygram_pipeline(3, wordsPerSentence)
    model=MLE(3)
    model.fit(train,vocab)
    print("Trigramm sentences\n")
    for i in range(10):
        print("Sentence {}".format(i))
        print(generate(model, num_words=random.randint(10,20), random_seed=random.randint(0,50)))
        print("\n")

def bigrammSentences(wordsPerSentence):
    train, vocab = padded_everygram_pipeline(2, wordsPerSentence)
    model = MLE(2)
    model.fit(train, vocab)
    print("Bigramm sentences\n")
    for i in range(10):
        print("Sentence {}".format(i))
        print(generate(model, num_words=random.randint(10,20), random_seed=random.randint(0,50)))
        print("\n")

def generate(model, num_words, random_seed):
    detokenize = TreebankWordDetokenizer().detokenize
    content = []
    for token in model.generate(num_words, random_seed=random_seed):
        if token == '<s>':
            continue
        if token == '</s>':
            break
        content.append(token)
    return detokenize(content)


if __name__ == '__main__':
    ###### For downloading the data#########
    #downloaddata('gutenberg')
    #############################
    files=gutenberg.fileids()
    myFiles=files[:10]
    rawText=gutenberg.raw(myFiles)
    words, wordsPerSentence, sentences=tokenization(rawText)
    Freq(words,"unigramm.txt")
    bigramms(wordsPerSentence)
    trigramms(wordsPerSentence)
    trigrammsSentences(wordsPerSentence)
    bigrammSentences(wordsPerSentence)