import csv
import sklearn
import pickle
import yaml
from os import listdir
from os.path import isfile, join
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB


import numpy as np


onlyfiles = [f for f in listdir('../FinalData/all yaml')
             if isfile(join('../FinalData/all yaml', f))]

x=[]
Y =[]



model =GaussianNB()

with open('Data/' + 'xfile' + '.txt',
          'rb') as f:
    x = pickle.load(f)
with open('Data/' + 'yfile' + '.txt',
          'rb') as f:
    Y = pickle.load(f)
x=np.array(x)
Y=np.array(Y)
x=x.tolist()
#removing Some

for i in range(len(x)):
     x[i].pop(0)
     #x[i].pop(0)

     x[i].pop(0)
     x[i].pop(2)
     x[i].pop(3)
     x[i].pop(2)

     x[i].pop(2)

x_train=x[0:2885]
x_predict=x[2886:]
y_train=Y[0:2885]
y_predict=Y[2886:]


x=np.array(x_train)
Y=np.array(y_train)
model.fit(x, Y)
print(len(x))
print(len(Y))

lstacul = []
lstapredt = []
for i in range(len(x_predict)):


    #arr=np.array([x_train[i]])


    #tossdecison = data['info']['toss']['decision']
    win=y_predict[i]
    lstacul.append(win)



    check=model.predict([x_predict[i]])
    lstapredt.append(check)


cout=0
for i in range(len(lstacul)):
    if lstapredt[i]==lstacul[i]:
        cout+=1

print('Accuracy',(cout/len(lstacul))*100)
from sklearn.metrics import accuracy_score
print(accuracy_score(lstacul, lstapredt)*100)
