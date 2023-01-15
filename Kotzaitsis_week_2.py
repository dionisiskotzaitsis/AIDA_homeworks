import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import metrics



def getDataset():
    breast = load_breast_cancer()
    breast_data = breast.data
    breast_labels = breast.target
    labels = np.reshape(breast_labels, (569, 1))
    final_breast_data = np.concatenate([breast_data, labels], axis=1)
    breast_dataset = pd.DataFrame(final_breast_data)
    features = breast.feature_names
    features_labels = np.append(features, 'label')
    breast_dataset.columns = features_labels
    print(features)
    #breast_dataset['label'].replace(0, 'Benign', inplace=True)
    #breast_dataset['label'].replace(1, 'Malignant', inplace=True)
    return breast_dataset,features


def pca(dataset,features):
    x = dataset.loc[:, features].values
    x = StandardScaler().fit_transform(x)
    i=1
    while i!=0:
        pca_breast = PCA(n_components=i)
        principalComponents_breast = pca_breast.fit_transform(x)
        principal_breast_Df = pd.DataFrame(data=principalComponents_breast)
        if sum(pca_breast.explained_variance_ratio_)>=0.75:
            print(sum(pca_breast.explained_variance_ratio_) )
            i=0
        else:
            i=i+1

    principal_breast_Df['label']=list(dataset['label'])

    return principal_breast_Df,pca_breast.explained_variance_ratio_


def splitData(dataset):
    trainindexes=[]
    testindexes=[]
    ben=int(list(dataset['label']).count(0.0)*0.85)
    mal=int(list(dataset['label']).count(1.0)*0.85)
    mlist=list(dataset['label'])
    j=0
    for i in range(len(mlist)):
        if j==ben:
            break
        elif mlist[i]==0.0:
            trainindexes.append(i)
            j=j+1

    j=0
    for i in range(len(mlist)):
        if j==mal:
            break
        elif mlist[i]==1.0:
            trainindexes.append(i)
            j=j+1

    for i in range(len(mlist)):
        if i not in trainindexes:
            testindexes.append(i)


    return ben,mal,trainindexes,testindexes


def spliting(dataset,trainindex,testindex):
    train=dataset.loc[trainindex]
    test=dataset.loc[testindex]
    return train,test


def modeling(train,test):
    lr=LogisticRegression( max_iter=10000)
    x_train=train.drop('label',1)
    x_test=test.drop('label',1)
    print(len(x_test))
    lr.fit(x_train,train['label'])
    pred=lr.predict(x_test)
    acc = metrics.accuracy_score(test['label'], pred)
    cm = metrics.confusion_matrix(test['label'], pred)
    print(acc)
    print(cm)
    return 0

if __name__ == '__main__':
    breast_dataset,features=getDataset()
    print(breast_dataset)
    pca_breast,var_ratio=pca(breast_dataset,features)
    print(pca_breast,var_ratio)

    ##########################################################
    benign,malignant,trainindex,testindex=splitData(breast_dataset)
    train,test=spliting(pca_breast,trainindex,testindex)
    modeling(train,test)
    ##########################################################

    train2,test2=spliting(breast_dataset,trainindex,testindex)
    modeling(train2,test2)