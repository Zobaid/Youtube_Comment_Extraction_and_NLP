import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
import requests 


url="https://www.youtube.com/watch?v=icetLikj7XY"
data=[]

with Chrome('C:/Users/Ultimate-SK/Desktop/Zobaid/Selenium/chromedriver.exe') as driver:
    wait = WebDriverWait(driver,5)
    driver.get(url)

    #for item in range(190): 
       # wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
       # time.sleep(10)

    #for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
     #   data.append(comment.text)
    

    	
    	# getting the request from url 
#r = requests.get(url) 
    	
    	# converting the text 
#s = BeautifulSoup(r.text, "html.parser") 
    	
    	# finding meta info for title 
#title = s.find("span", class_="watch-title").text.replace("\n", "") 
    	
    	# finding meta info for views 
#views = s.find("div", class_="watch-view-count").text 
    	
    	# finding meta info for likes 
#likes = s.find("span", class_="like-button-renderer").span.button.text 
    	
    	# saving this data in dictionary 
#datas = {'title':title, 'views':views, 'likes':likes} 
number_of_likes = driver.find_element_by_xpath("#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a > yt-formatted-string").text
    	
    	# returning the dictionary 
    	
    
    
    	
    	# calling the function 
    	#data = scrape_info(url) 
    	
    	# printing the dictionary 
#print(datas) 

import pandas as pd   
#df = pd.DataFrame(data, columns=['comment'])
#dfs=pd.DataFrame(datas,columns=['title','views','likes'])
    
#df.to_csv(r'addidas3.csv',index=False, header=True) 
#dfs.to_csv(r'addidas3a.csv',index=False, header=True)   
print(number_of_likes)
print ("done")
    



    