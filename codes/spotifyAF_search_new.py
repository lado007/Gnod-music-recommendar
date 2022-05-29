#!/usr/bin/env python
# coding: utf-8

# In[28]:


def spotify():
    #import libraries
    import spotipy 
    from spotipy.oauth2 import SpotifyClientCredentials
    import getpass
    client_id=str(getpass.getpass('enter your client id?'))
    client_secret=str(getpass.getpass('enter your client secret?'))
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret))
    
    import pandas as pd
    scaled_df=pd.read_csv('audio_df')
    scaled_df.drop(['Unnamed: 0'], inplace=True, axis=1)
    
    
    
    
    
    #search song uri
    results=sp.search(q=input('enter song name? :'),limit=1, type='track')
    name=results['tracks']['items'][0]['name']
    artist=results['tracks']['items'][0]["artists"][0]["name"]
    uri = results['tracks']['items'][0]['uri']
    
    #get audio features
    audio_feat_inputsong=sp.audio_features(tracks=uri)
    audio_feat_dict=audio_feat_inputsong[0]
    af_df=pd.DataFrame.from_dict([audio_feat_dict])
    af_df.drop(['track_href','type','id','uri','analysis_url','time_signature'], inplace=True, axis=1)
    
    from sklearn.preprocessing import MinMaxScaler
    scaler=MinMaxScaler()
    scaler.fit(scaled_df)
    array_df=scaler.transform(af_df)
    search_df=pd.DataFrame(array_df,columns=['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'duration_ms'])
    return search_df
    
    


# In[29]:


spotify()


# In[ ]:





# In[ ]:




