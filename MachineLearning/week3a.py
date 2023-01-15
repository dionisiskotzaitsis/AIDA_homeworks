import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix


def splitData(dataset):
    trainindexes = []
    testindexes = []
    surv = int(list(dataset['Survived']).count('Yes') * 0.80)
    died = int(list(dataset['Survived']).count('No') * 0.80)
    mlist = list(dataset['Survived'])
    j = 0
    for i in range(len(mlist)):
        if j == surv:
            break
        elif mlist[i] == 'Yes':
            trainindexes.append(i)
            j = j + 1

    j = 0
    for i in range(len(mlist)):
        if j == died:
            break
        elif mlist[i] == 'No':
            trainindexes.append(i)
            j = j + 1

    for i in range(len(mlist)):
        if i not in trainindexes:
            testindexes.append(i)

    return surv, died, trainindexes, testindexes


def spliting(dataset, trainindex, testindex):
    train = dataset.loc[trainindex]
    test = dataset.loc[testindex]
    return train, test


def DecisionTree(train, test):
    clf = DecisionTreeClassifier(random_state=0)
    X_train = train.loc[:, train.columns != 'Survived']
    Y_train = train['Survived']
    X_test = test.loc[:, test.columns != 'Survived']
    Y_test = test['Survived']
    clf = clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    evaluation(y_pred, Y_test)


def evaluation(pred, Y_test):
    print("Accuracy:", metrics.accuracy_score(Y_test, pred))
    print(pd.crosstab(Y_test, pred))


def dfChange(df):
    df["Age"].replace({"Adult": 1, "Child": 0}, inplace=True)
    df["Class"].replace({"First": 0, "Second": 1, "Third": 2, "Crew": 3}, inplace=True)
    df["Sex"].replace({"Male": 0, "Female": 1}, inplace=True)

    print(df)


if __name__ == '__main__':
    df = pd.read_excel("Titanic.xlsx", engine='openpyxl')
    df=df.drop([0,1])
    df.index = pd.RangeIndex(len(df.index))
    print(df.columns)
    print(df['Class'].values)
    print(df)
    dfChange(df)
    survived, died, trainindex, testindex = splitData(df)
    train, test = spliting(df, trainindex, testindex)
    DecisionTree(train, test)
