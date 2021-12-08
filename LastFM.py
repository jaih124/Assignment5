# LastFM.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

import urllib, json
from urllib import request,error
from WebAPI import WebAPI

class LastFM(WebAPI):
    def __init__(self, artist="NAV"):
        self._artist = artist
        self._apikey = ""
        self._response_dict = []
        
        super().__init__()
        
    def load_data(self) -> None:
      '''
      Calls the web api using the required values and stores the response in class data attributes.
            
      '''
      #TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
      #TODO: assign the necessary response data to the required class data attributes
      artist = self._artist
      apikey = self._apikey
      api_call = f'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={apikey}&format=json'

      music_dict = LastFM.download_url(api_call)

      for key in music_dict.keys():
          if key == 'toptracks':
              inside_dict = music_dict[key]
              
              for key2, value2 in music_dict.items():
                  d = {key2: value2['track'][0]['name']}
                  self.__dict__.update(d)

    def transclude(self, message: str) -> str:
        transclude = self.transclude
        artist = self._artist
        apikey = "18952f825c28063e293753cff5fb8c19"
        get_music = LastFM(artist)
        get_music.set_apikey(apikey)
        get_music.load_data()
        replace_music = f"The top track for {artist} is {get_music.toptracks}."
        message = message.replace("@lastfm", replace_music)
        self.message = message
        return message
