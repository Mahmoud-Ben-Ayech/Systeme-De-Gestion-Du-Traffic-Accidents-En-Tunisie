import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome()
browser.maximize_window() # For maximizing window
#driver = webdriver.Chrome(PATH)
browser.get("https://www.twitter.com/login?lang=en")
subject = "Harassement"


# Setup the log in
sleep(10)
username = browser.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("put_your_email_or_username_here")    #you must modify this case by your email or yousrname in X platforme 
wait = WebDriverWait(browser, 5) 
next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
next_button.click()
sleep(3)
username = browser.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("user_name")  #Remplacer ceci par le nom de l'utilisateur 
username = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
username.click()
sleep(10)
password =browser.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('user_password')   #Remplacez ceci par la Mot de passe 
log_in = browser.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(3)
browser.get("https://twitter.com/search?q=%23accidents%20%23tunisie&src=typed_query&f=top?lang=en")
UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]


articles = browser.find_elements(By.XPATH,"//article[@data-testid='tweet']")
start_time = time.time()
while time.time() - start_time < 30: 
    for article in articles:
        UserTag = browser.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        UserTags.append("UserTag")
        TimeStamp = browser.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        Tweet = browser.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        Reply = browser.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        reTweet = browser.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        Like = browser.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = browser.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break
print(len(UserTags),
len(TimeStamps),
len(Tweets),
len(Replys),
len(reTweets),
len(Likes))


    
import pandas as pd
#df = pd.DataFrame(pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes),columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes']))
df = pd.DataFrame(pd.DataFrame(zip(TimeStamps,Tweets),columns=['Date','Evenement']))
df.head()
browser.quit()

from pymongo import MongoClient

df['_id'] = range(1, len(df) + 1)

df['Titre'] = 'annonce twitter'

df = df.drop_duplicates(subset='Evenement')

client = MongoClient('mongodb://localhost:27017')
db = client['db_soc']
collection = db['twitter']

records = df.to_dict(orient='records')

collection.delete_many({})

collection.insert_many(records)

client.close()
