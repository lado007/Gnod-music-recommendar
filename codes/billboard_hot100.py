#!/usr/bin/env python
# coding: utf-8

# In[9]:


def billboard_data():
    
    #1. import our libraries
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup 
    
    #2. find url and store it in a variable
    url = "https://www.billboard.com/charts/hot-100"
    
    #3. download html with a get request
    page = requests.get(url)
    if page.status_code != 200:
        print("Scraping failed. Status code " + str(page.status_code))
        
    #4. parse html (create the 'soup')
    soup = BeautifulSoup(page.content, "html.parser")
    
    #5. selecting specific variables 
    songs=soup.select('h3.c-title.a-no-trucate')[14].get_text(strip = True)
    artists=soup.select('span.c-label.a-no-trucate')[14].get_text(strip = True)
    
    #6. checking if the length of the two variables
    len_songtitle=len(soup.select('h3.c-title.a-no-trucate'))
    len_artist=len(soup.select('span.c-label.a-no-trucate'))
    if len_songtitle != len_artist:
        print('index do not match,please check length of variables')
    
    #7. appending the data into columns and rank
    song_rank=[]
    song_title=[]
    Artist=[]

    for i in (range(len_songtitle)):
        song_rank.append(i+1)
        song_title.append(soup.select('h3.c-title.a-no-trucate')[i].get_text(strip = True))
        Artist.append(soup.select('span.c-label.a-no-trucate')[i].get_text(strip = True))
        
    #8. putting data into a dataframe
    top_100_songs = pd.DataFrame({'rank':song_rank,
                           'song':song_title,
                           'artist':Artist})
    return top_100_songs
    
    
    
     


# In[ ]:




