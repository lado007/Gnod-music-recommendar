#!/usr/bin/env python
# coding: utf-8

# In[203]:


def music_recommender():
    #1. import libraries and defined .py funtions
    from billboard_hot100 import billboard_data
    from song import song
    import spotipy 
    from spotipy.oauth2 import SpotifyClientCredentials
    from IPython.core.display import display
    from IPython.display import IFrame
    import getpass
    import numpy 
    from sklearn.cluster import KMeans
    client_id=str(getpass.getpass('enter your client id?'))
    client_secret=str(getpass.getpass('enter your client secret?'))
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret))
    
    import pandas as pd
    from sklearn.cluster import KMeans
    from random import randint
    
    
    #. assign functions to a variable
    billboard = billboard_data()
    song=song()
    
        
    #. check if song is on billboard hot 100
    result=billboard[billboard['song'].str.contains(song)]
    
    #. getting the index of our result
    index = result.index.tolist()
    
    
    #. check if cell is empty
    if len(song) < 1:
        print('you did not enter a song')
        return
    
    
    #. using the index of the resulting search to get our song title and artist from the data frame
    #we cant use loc or iloc function (top_100_songs.loc[ index , song ])in this case as it would return a KeyError
        billboard.song[index].values[0]
        billboard.artist[index].values[0]
    if len(index) > 0:  
        answer = input('did you mean ' + billboard.song[index].values[0] + ' by ' + billboard.artist[index].values[0] + '?: ')
        recommendar = billboard.sample().index.tolist() #. using the python random sample() function to select randomly from our database  for recommendations if answer is yes
        if answer.lower() == 'yes':
                print('Great!, you might also like ' + billboard['song'][recommendar].values[0] + ' by ' + billboard['artist'][recommendar].values[0])
    elif index ==[]:
        question=input('sorry,that is not amongst the top songs right now,would you like to listen to a similar recommended music from spotify?: ')
        if question.lower() == 'yes': 
                audio_df=pd.read_csv('audio_df')
                audio_df.drop(['Unnamed: 0'], inplace=True, axis=1)
                scaled_df=pd.read_csv('scaled_df2')
                scaled_df.drop(['Unnamed: 0'], inplace=True, axis=1)
                audiof_df=pd.read_csv('audio_dfurl')
                audiof_df.drop(['Unnamed: 0'], inplace=True, axis=1)
        #search song uri
                results=sp.search(q=(song),limit=1, type='track')    
                uri = results['tracks']['items'][0]['uri']    
     #get audio features
                audio_feat_inputsong=sp.audio_features(tracks=uri)
                audio_feat_dict=audio_feat_inputsong[0]
                af_df=pd.DataFrame.from_dict([audio_feat_dict])
                af_df.drop(['track_href','type','id','uri','analysis_url','time_signature'], inplace=True, axis=1)
                from sklearn.preprocessing import MinMaxScaler
                scaler=MinMaxScaler()
                scaler.fit(audio_df)
                array_df=scaler.transform(af_df)
                search_df=pd.DataFrame(array_df,columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
                'duration_ms'])
      # run kmeans to fit to our old data frame (correct of clusters )
                kmeans=KMeans(n_clusters=49, random_state=5)
                kmeans.fit(scaled_df)
                search=  kmeans.predict(search_df)
                recommender=audiof_df[audiof_df.cluster==search[0]].sample(1)
                recommender['id'].values[0]
                display(IFrame(src=f'https://open.spotify.com/embed/track/'+recommender['id'].values[0],
                width='500',height='100',
                frameborder='10',
                allowtransparency='true',
                allow='encrypted-media',))
           
        else:
                print('sorry,you can try a new song, thanks ')
         
        
        
        
    
    
    


# In[208]:


music_recommender()


# In[ ]:




