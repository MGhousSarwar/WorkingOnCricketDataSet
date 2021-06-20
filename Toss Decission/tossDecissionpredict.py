import csv
import sklearn
import pickle
import yaml
from os import listdir
from os.path import isfile, join
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LinearRegression


import numpy as np


onlyfiles = [f for f in listdir('../FinalData/all yaml')
             if isfile(join('../FinalData/all yaml', f))]

x=[]
Y =[]






model = GaussianNB()

with open('Data/' + 'xfile' + '.txt',
          'rb') as f:
    x = pickle.load(f)
with open('Data/' + 'yfile' + '.txt',
          'rb') as f:
    Y = pickle.load(f)

x=np.array(x)
Y=np.array(Y)

x_train=x[0:3975]
x_predict=x[3976:]

y_train=Y[0:3975]
y_predict=Y[3976:]

#removing matchtype from x data
# for i in range(len(x)):
#     x[i].pop(0)

x=np.array(x_train)
Y=np.array(y_train)

model.fit(x, Y)

#y=(f(x))
print(len(x))
print(len(Y))

lstacul = []
lstapredt = []
for i in range(len(x_predict)):


    tossdecison=y_predict[i]
    if  tossdecison==1:
        tossdecison=1
        print('accutal : bat')
        lstacul.append('bat')

    else:
        tossdecison=0
        print('accutal : bowl')
        lstacul.append('bowl')


    check=model.predict([x_predict[i]])
    if check==1:
        print('predicted : bat' )
        lstapredt.append('bat')
    else:
        print('predicted : bowl')
        lstapredt.append('bowl')
cout=0
for i in range(len(lstacul)):
    if lstapredt[i]==lstacul[i]:
        cout+=1

print('Accuracy',int((cout/len(lstacul))*100),'%')

from sklearn.metrics import accuracy_score
print((int(accuracy_score(lstacul, lstapredt)*100)),'%')


#here you can predict by giving your own data
# matchtype='T20'
# matchtype = [ord(c) for c in matchtype]
# matchtype = sum(matchtype)
# t1 = [ord(c) for c in 'India']
# t1 = sum(t1)
# t2 = [ord(c) for c in 'Pakistan']
# t2 = sum(t2)
#
# tosswin='Pakistan'
# tosswin = [ord(c) for c in tosswin]
# tosswin = sum(tosswin)
# custom=model.predict([[matchtype,t2,t1,tosswin]])
# print(custom)