import nltk
from nltk.corpus import movie_reviews,stopwords
from nltk.classify import NaiveBayesClassifier
import collections
from nltk.metrics import precision,recall,f_measure,ConfusionMatrix

def create_word_features(words):
    stopW=stopwords.words("english")
    useful_words = [word for word in words if word not in stopW]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

if __name__ == '__main__':
    print(movie_reviews.categories())
    neg_reviews = []
    pos_reviews = []
    for fileid in movie_reviews.fileids('neg'):
        words = movie_reviews.words(fileid)
        neg_reviews.append((create_word_features(words), "negative"))

    for fileid in movie_reviews.fileids('pos'):
        words = movie_reviews.words(fileid)
        pos_reviews.append((create_word_features(words), "positive"))

    train = neg_reviews[:1200] + pos_reviews[:1200]
    test_set = neg_reviews[400:] + pos_reviews[400:]



    classifier = NaiveBayesClassifier.train(train)
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)

    for i, (feats, label) in enumerate(test_set):
        print(i, (feats, label))
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)


    accuracy = nltk.classify.util.accuracy(classifier, test_set)
    print("accuracy",accuracy)
    print('positive precision:', precision(refsets['positive'], testsets['positive']))
    print('positive recall:', recall(refsets['positive'], testsets['positive']))
    print('positive F-measure:', f_measure(refsets['positive'], testsets['positive']))
    print('negative precision:', precision(refsets['negative'], testsets['negative']))
    print('negative recall:', recall(refsets['negative'], testsets['negative']))
    print('negative F-measure:', f_measure(refsets['negative'], testsets['negative']))
