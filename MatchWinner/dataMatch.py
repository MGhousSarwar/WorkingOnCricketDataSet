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

for i in range(len(onlyfiles)):
    print('reading : ',i)
    print(onlyfiles[i])
    file = '../FinalData/all yaml/' + onlyfiles[i]
    data = yaml.load(open(file, 'r').read(),yaml.Loader)

    try:
        city=data['info']['city']
        city = [ord(c) for c in city]
        city = sum(city)

        venue=data['info']['venue']
        venue = [ord(c) for c in venue]
        venue = sum(venue)

        matchtype=data['info']['match_type']
        matchtype = [ord(c) for c in matchtype]
        matchtype = sum(matchtype)

        teams=data['info']['teams']
        t1 = [ord(c) for c in teams[0]]
        t1 = sum(t1)
        t2 = [ord(c) for c in teams[1]]
        t2 = sum(t2)

        tossdecison = data['info']['toss']['decision']
        decision = tossdecison[0]
        if decision =='bat':
            decision=1
        else:
            decision=0

        tosswin = [ord(c) for c in tossdecison[0]]
        tosswin = sum(tosswin)

        overs = data['info']['overs']



        arr=[city,matchtype,t1,t2,decision,tosswin,overs,venue]

        winner = data['info']['outcome']['winner']
        winner = [ord(c) for c in winner]
        winner = sum(winner)

        x.append(arr)

        Y.append(winner)
    except:
        pass


with open('Data/' + 'xfile' + '.txt', 'wb') as f:
    pickle.dump(x, f)
with open('Data/' + 'yfile' + '.txt', 'wb') as f:
    pickle.dump(Y, f)