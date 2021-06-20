import os
import csv
import sklearn
import pickle
import yaml
from BallByBall.BowlerClass import *
from os import listdir
from os.path import isfile, join




def checkforbowler(bowler):
    for i in range(len(lst)):
        if bowler==lst[i].Name:
            #exist
            return i
    lst.append(Structure(bowler))
    return len(lst)-1

def checkforcombo(index,combo):
    for i in range(len(lst[index].combolst)):
        if combo[0]==lst[index].combolst[i].Batsman and combo[1]==lst[index].combolst[i].Runner:
            #exist
            return i
    lst[index].addcombo(combo[0], combo[1])
    return len(lst[index].combolst)-1

def MainMeth(f):
    global  lst
    file = '../FinalData/all yaml/'+f
    data = yaml.load(open(file, 'r').read(),yaml.Loader)
    innings=data['innings']
    print(len(innings))
    if len(innings)>2:
        print(innings)

    for x in range(len(innings)):
        set=str(x+1)
        if set=='1':
            set='1st'
        elif set=='2':
            set='2nd'
        elif set=='3':
            set='3rd'
        elif set=='4':
            set='4th'
        elif set=='5':
            set='5th'
        elif set == '6':
            set = '6th'
        elif set == '7':
            set = '7th'
        elif set == '8':
            set = '8th'
        try:
            innings1 = data['innings'][x][set+' innings']['deliveries']
            for row in innings1:
                    bowler = row[next(iter(row))]['bowler']
                    batmans = [row[next(iter(row))]['batsman'],
                               row[next(iter(row))]['non_striker']]
                    runs = row[next(iter(row))]['runs']['batsman']

                    index = checkforbowler(bowler)
                    index2 = checkforcombo(index, batmans)

                    lst[index].combolst[index2].addrun(runs)
                    with open('BallByBall/Data/' + bowler + '.txt',
                              'wb') as f:
                        # var = {1 : 'a' , 2 : 'b'}
                        pickle.dump(lst[index], f)
        except Exception:
            pass

        # print(bowler)
        # print(lst[0].combolst[0].most_common())

onlyfiles = [f for f in listdir('../FinalData/all yaml')
             if isfile(join('../FinalData/all yaml', f))]
lst=[]

for i in range(len(onlyfiles)):
    print('Doing : '+str(onlyfiles[i]))

    MainMeth(onlyfiles[i])
    print('List Count : '+str(len(lst)))
    print('Remaning Files : '+str(len(onlyfiles)-1-i))



