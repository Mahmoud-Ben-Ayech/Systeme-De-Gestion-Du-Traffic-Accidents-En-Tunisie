import requests
from bs4 import BeautifulSoup
import pymongo


headers = {
         'User-Agent': 'a'
    }
url = 'https://lapresse.tn/tag/trafic-routier/'


client=pymongo.MongoClient('localhost',27017)
myDb = client["db_soc"]
myTable = myDb["Event"]

myTable.delete_many({})


def get_soup_event(even):
    lien_vers_event=even.find('a').get('href')
    r_event=requests.get(lien_vers_event,headers=headers)
    soup_event=BeautifulSoup(r_event.content,"html.parser")
    return soup_event


def get_event_content(even,soup_event):
    content_events=soup_event.find('div', class_='bdaia-post-content').find_all('span',class_='s1')
    content_ev=''
    if content_events :
        for ce in content_events :
            content_ev=content_ev + ce.text + '\n'   
    else :
        content_ev=even.find('p').text  
    return content_ev    


def get_element() :
    
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    
    events=soup.find_all('div', class_='block-article bdaiaFadeIn')
    
    event_tab=[]
    countId=1
    for even in events :
        soup_event=get_soup_event(even)

        title=even.find('h2').text
        event_date=soup_event.find('div', class_='bdaia-post-date').find('span',class_='bdayh-date').text
        content_ev=get_event_content(even,soup_event)

        event_tab.append({'_id':countId,'Titre':title,'Date':event_date,'Evenement':content_ev})
        countId+=1
    myTable.insert_many(event_tab)

 
get_element()

