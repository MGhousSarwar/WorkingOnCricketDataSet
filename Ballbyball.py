import pickle
import yaml

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('../FinalData/all yaml/')
             if isfile(join('../FinalData/all yaml/', f))]

TA=[]
PA=[]
def PerformTaks(no):

    for ii in range(0,no):
        lstacul = []
        lstapredt = []
        file = '../FinalData/all yaml/' + onlyfiles[ii]
        data = yaml.load(open(file, 'r').read(),yaml.Loader)
        innings = data['innings']
        for x in range(len(innings)):
            set = str(x + 1)
            if set == '1':
                set = '1st'
            elif set == '2':
                set = '2nd'
            elif set == '3':
                set = '3rd'
            elif set == '4':
                set = '4th'
            elif set == '5':
                set = '5th'
            elif set == '6':
                set = '6th'
            elif set == '7':
                set = '7th'
            elif set == '8':
                set = '8th'
            try:
                innings1 = data['innings'][x][set + ' innings']['deliveries']
                for row in innings1:
                    bowler = row[next(iter(row))]['bowler']
                    batmans = [row[next(iter(row))]['batsman'],
                               row[next(iter(row))]['non_striker']]
                    runs = row[next(iter(row))]['runs']['batsman']

                    with open('Data/' + bowler+'.txt',
                              'rb') as f:
                        var = pickle.load(f)

                        for i in range(len(var.combolst)):
                            if var.combolst[i].Batsman==batmans[0] and var.combolst[i].Runner == batmans[1]:
                                # print('Actual : ' ,runs, " predicted run :",var.combolst[i].most_common())
                                lstapredt.append(var.combolst[i].most_common())
                                lstacul.append(runs)

            except Exception:
                pass

        from sklearn.metrics import accuracy_score
        try:
            print('                           Match',ii+1,'Accuracy is :',accuracy_score(lstacul, lstapredt)*100,'%')
        except:
            pass


        # lsterr=[]
        # cout=0
        # for i in range(len(lstapredt)):
        #     errr=abs(lstacul[i]-lstapredt[i])
        #     lsterr.append(errr)



        # err=sum(lsterr)
        # err=(err/len(lstapredt))*100
        # # print('Up To : ',ii+1,' : ',100-err)

no=input('Enter No of Matches To be check.')
PerformTaks(int(no))
