import pandas as pd
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

def splitData(dataset):
    trainindexes=[]
    testindexes=[]
    one=int(list(dataset['Outcome']).count(1)*0.8)
    zero=int(list(dataset['Outcome']).count(0)*0.8)
    mlist=list(dataset['Outcome'])
    print("mlist",mlist)
    j=0
    for i in range(len(mlist)):
        if j==one:
            break
        elif mlist[i]==1:
            trainindexes.append(i)
            j=j+1

    j=0
    for i in range(len(mlist)):
        if j==zero:
            break
        elif mlist[i]==0:
            trainindexes.append(i)
            j=j+1

    for i in range(len(mlist)):
        if i not in trainindexes:
            testindexes.append(i)

    print("trainindexes",trainindexes)
    print("test", testindexes)

    return one,zero,trainindexes,testindexes


def spliting(dataset,trainindex,testindex):
    train=dataset.loc[trainindex]
    test=dataset.loc[testindex]
    return train,test


def kMeans(train,k,mydist):
    X_train = train.loc[:, train.columns != 'Outcome']
    Y_train = train['Outcome']
    X_test = test.loc[:, test.columns != 'Outcome']
    Y_test = test['Outcome']
    neigh = KNeighborsClassifier(n_neighbors=int(k),metric=str(mydist))
    neigh.fit(X_train,Y_train)
    y_pred=neigh.predict(X_test)
    evaluateKMeans(Y_test,y_pred)

def evaluateKMeans(Y_test,pred):
    print("Accuracy:", metrics.accuracy_score(Y_test, pred))
    print(pd.crosstab(Y_test, pred))

if __name__ == '__main__':
    df = pd.read_csv('diabetes_data.csv', sep=",")
    one,zero,trainindexes,testindexes=splitData(df)
    train,test=spliting(df, trainindexes, testindexes)
    k=input("Give me your k list separated by comma. Press enter to continue\n")
    dis = input("Give me your distance metric list separated by comma. Press enter to continue.\n")
    kM=k.strip().split(',')
    disM=dis.strip().split(',')
    for dis in disM:
        print("##############", dis, "################\n")
        for k in kM:
            print("##############", k, "################\n")
            kMeans(train, k, dis)

