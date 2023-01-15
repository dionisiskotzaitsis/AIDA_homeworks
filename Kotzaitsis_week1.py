import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

j=[]
for i in range(0,30):
    if i<10:
        j.append('mean')
    elif i>=10 and i<20:
        j.append('std. error')
    else:
        j.append('worst')


categories=['radius','texture','perimeter','area','smoothness','compactness','concavity','concave points','symmetry','fractal dimension']
cols=[]
cols.append('index')
cols.append('Diagnosis')
counter=0
for i in range(0,30):
    if counter<=9:
        cols.append(str(j[i]+' '+categories[counter]))
        counter=counter+1
    else:
        counter=0
        cols.append(str(j[i] + ' ' + categories[counter]))
        counter=counter+1



df = pd.read_csv('wdbc.data', sep=",",header=None,names=cols,index_col='index')
######################
print("a ερωτημα")

df_one = pd.get_dummies(df['Diagnosis'])
df_two = pd.concat((df_one, df), axis=1)
df_two = df_two.drop(['Diagnosis'], axis=1)
df_two = df_two.drop(["B"], axis=1)
result = df_two.rename(columns={"M": 'Diagnosis'})
print(result)


######################
print("b ερωτημα")

a=result.groupby('Diagnosis')
print(a.describe())
for i in range(2,32):
    print(a[cols[i]].describe(),a[cols[i]].var())

######################
print("c ερωτημα")
mean=a.mean()
var=a.var()
print("mean",mean)
print("variance",var)

meanPlt=mean.plot(kind='bar',legend=None,title="Mean Plot")
meanPlt.legend(loc=9)
plt.show()

varPlt=var.plot(kind='bar',legend=None,title="Variance Plot")
plt.show()

######################
print("d ερωτημα")

y=result['Diagnosis']
X=result[cols[2:]]

logreg = LogisticRegression(solver='lbfgs', max_iter=10000)
logreg.fit(X,y)
print(logreg.coef_)