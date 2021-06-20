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

for i in range(len(onlyfiles)):
    print('reading : ',i)
    file = '../FinalData/all yaml/' + onlyfiles[i]
    data = yaml.load(open(file, 'r').read(),yaml.Loader)

    matchtype=data['info']['match_type']
    matchtype = [ord(c) for c in matchtype] #[ODI=61,63,64]
    matchtype = sum(matchtype)

    teams=data['info']['teams']
    t1 = [ord(c) for c in teams[0]]
    t1 = sum(t1)
    t2 = [ord(c) for c in teams[1]]
    t2 = sum(t2)

    tosswin=data['info']['toss']['winner']
    tosswin = [ord(c) for c in tosswin]
    tosswin = sum(tosswin)

    arr=[matchtype,t1,t2,tosswin]
    x.append(arr)

    tossdecison = data['info']['toss']['decision']
    if  tossdecison=='bat':
        tossdecison=1
    else:
        tossdecison=0
    Y.append(tossdecison)

with open('Data/' + 'xfile' + '.txt', 'wb') as f:
    pickle.dump(x, f)
with open('Data/' + 'yfile' + '.txt', 'wb') as f:
    pickle.dump(Y, f)