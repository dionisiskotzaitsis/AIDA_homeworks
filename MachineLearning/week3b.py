import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix


def splitData(dataset):
    trainindexes=[]
    testindexes=[]
    sick=int(list(dataset['class']).count('sick')*0.75)
    healthy=int(list(dataset['class']).count('healthy')*0.75)
    mlist=list(dataset['class'])
    j=0
    for i in range(len(mlist)):
        if j==sick:
            break
        elif mlist[i]=='sick':
            trainindexes.append(i)
            j=j+1

    j=0
    for i in range(len(mlist)):
        if j==healthy:
            break
        elif mlist[i]=='healthy':
            trainindexes.append(i)
            j=j+1

    for i in range(len(mlist)):
        if i not in trainindexes:
            testindexes.append(i)


    return sick,healthy,trainindexes,testindexes


def spliting(dataset,trainindex,testindex):
    train=dataset.loc[trainindex]
    test=dataset.loc[testindex]
    return train,test


def DecisionTree(train,test):
    clf=DecisionTreeClassifier(random_state=0)
    X_train=train.loc[:, train.columns != 'class']
    Y_train=train['class']
    X_test=test.loc[:, test.columns != 'class']
    Y_test=test['class']
    clf=clf.fit(X_train,Y_train)
    y_pred=clf.predict(X_test)
    evaluation(y_pred,Y_test)

def evaluation(pred,Y_test):
    print("Accuracy:", metrics.accuracy_score(Y_test, pred))
    print(pd.crosstab(Y_test, pred))

def dfChange(df):
    df["sex"].replace({"Male": 1, "Female": 0}, inplace=True)
    df["chest pain type"].replace({"Angina": 0, "Abnormal Angina": 1, "NoTang":2, " Asymptomatic":3}, inplace=True)
    df["resting ecg"].replace({"Normal": 0, "Abnormal": 1,"Hyp":2}, inplace=True)
    df["slope"].replace({"Up": 0, "Flat": 1, "Down": 2}, inplace=True)
    df["thal"].replace({"Normal": 0, "Fix": 1, "Rev": 2}, inplace=True)

    print(df)

if __name__ == '__main__':
    df=pd.read_excel("Cardiology.xlsx",engine='openpyxl')
    print(df.columns)
    print(df)
    dfChange(df)
    sick, healthy, trainindex, testindex = splitData(df)
    train, test = spliting(df, trainindex, testindex)
    DecisionTree(train,test)
