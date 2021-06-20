from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import  datetime
from threading import *
import filebreaker
import threading
import time




class XYZ(Thread):

    done=0
    Remain=0
    def __init__(self,val):
        self.val=val
        self.d=0
        self.r=0
        self.percent=0
        Thread.__init__(self)
        #self.func(self.val)


    def run(self):
        self.func(self.val)

    def func(self,copy):
        link = self.get_link_scrap_data(copy)
        while (link != None):
            self.savedatavalues(link, copy)
            self.percent = (self.d / (self.d + self.r)) * 100
            #print('Thread :' + str(copy) + " Did Link:" + link)
            print('File :'+str(copy)+' Scrapped :'+str(int(self.percent))+' %'+' Done :'+str(self.d)+' Remaining :'+str(self.r))
            '''with open('tfinal' + str(copy) + '.csv', 'r') as file:
                alll = file.readlines()
                self.d=len(alll)
               # print('Done :' + str(done))'''
            link = self.get_link_scrap_data(copy)
        if link==None:
            return
            return

    def savedatavalues(self,my_url, copy):
        uclient = uReq(my_url)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html, "html.parser")
        # print(page_soup)
        with open('tfinal' + str(copy) + '.csv', 'a') as file:
            full_data = ['', '', '', '', '', '', '', '']

            for eachdiv in page_soup.find_all("p", {"class": "ciPlayerinformationtxt"}):
                # print(eachdiv)
                lines = str(eachdiv)
                head = ""
                data = ""
                status = False
                for d in range(len(lines)):
                    if (lines[d] == '<' and lines[d + 1] == 'b'):
                        d = d + 2
                        headmila = False
                        for e in range(d, len(lines)):
                            if lines[e] == '>':
                                for y in range(e + 1, len(lines)):
                                    if lines[y] != '<':
                                        head += lines[y]
                                    else:
                                        headmila = True
                                        break
                            elif headmila:
                                break
                    elif (lines[d] == '<' and lines[d + 1] == 's' and lines[d + 2] == 'p' and lines[d + 3] == 'a' and
                          lines[d + 4] == 'n'):
                        d = d + 5
                        for e in range(d, len(lines)):
                            if lines[e] == '>':
                                for y in range(e + 1, len(lines)):
                                    if lines[y] != '<':
                                        data += lines[y]
                                    else:
                                        status = True
                                        break
                            elif status:
                                break
                    elif status:
                        break
                data = data.replace('\n', '')
                data = data.replace(',', " ")
                # print(head+" : "+data)
                choices = {'Full name': 0,
                           'Born': 1,
                           'Current age': 2,
                           'Major teams': 3,
                           'Playing role': 4,
                           'Batting style': 5,
                           'Bowling style': 6,
                           'Relation': 7}
                full_data[choices.get(head, 7)] = data;
            for p in range(8):
                file.writelines(full_data[p])
                file.write(',')
            file.write('\n')

            #   print(s)
        #print("Completed at time: " + str(datetime.now()))
        self.d+=1
        file.close()

    def get_link_scrap_data(self,copy):
        #print("Do not Stop")

        f = open("player_" + str(copy) + ".txt", "r")
        lines = f.readlines()

        self.r=len(lines)-1
        #print('Remaining :' + str(remain) + ' <----> Time Required :' + str(remain / 3600))

       # print('Scrapping'+())

        f = open("player_" + str(copy) + ".txt", "w")
        for line in lines:
            if line != lines[0]:
                f.write(line)

        #print("stop now if u want")

        if (len(lines) == 0):
            return None
        else:
            larr=lines[0].split("\"")
            return larr[1]
import psutil
import os

# tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
#print("Memory Usage :")
#print("Total: "+str(tot_m)+" MB")
# print("Used : "+str(used_m)+" MB")
#print("Free : "+str(free_m)+" MB")
#print("CPU\n")
#print(str(psutil.cpu_percent())+" %")
noOfthread=int((psutil.virtual_memory().available -100)/10)
st=1
end=noOfthread+1

ff = open("player.txt", "r")
lines = ff.readlines()
ff.close()
lineperfile=int(len(lines)/end)+1


filebreaker.MAX_CHUNKS=lineperfile
filebreaker.main()

threads = [];

#break txt in noOfthreads txt's
for i in range(st,end):
    thread = XYZ(i)
    thread.setDaemon(True)
    threads.append(thread)
    thread.start();
for thread in threads:
    thread.join()

'''obj=XYZ(5)
obj.func(5)'''