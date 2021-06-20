from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from threading import  Thread
from datetime import  datetime

domain_name='http://www.espncricinfo.com'

def geturls():
    with open('Checking.txt', 'a') as file:#change  file name
        total=0
        for x in range(1, 2):  # country 1 to 50
            for y in range(65, 66):  # aplha A to Z
                char = chr(y)
                date=str(datetime.now())
                addr = 'http://www.espncricinfo.com/ci/content/player/country.html?country=' + str(x) + ';alpha=' + char
                print(date+': Main Link :'+addr)
                uclient = uReq(addr)
                page_html = uclient.read()
                uclient.close()
                page_soup = soup(page_html, "html.parser")
                # print(page_soup)
                i=1
                stringfull=""
                for div in page_soup.find_all("a",{"class":"ColumnistSmry"}):
                    string =str(div).split('"')
                    string=domain_name+string[3]
                    total=total+1
                    print('Country :'+str(x)+' Alpha :'+str(char)+" Link :"+string)
                   # print(str(i)+") Data Fetching From :"+string)
                    i=i+1
                    stringfull+=string+'\n'
                file.write(stringfull)
                print(' Total Links:'+str(total)+' Time Required :'+str(total/3600))



geturls()