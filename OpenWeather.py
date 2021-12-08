# OpenWeather.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

import urllib, json
from urllib import request,error
from WebAPI import WebAPI
from LastFM import LastFM        

class OpenWeather(WebAPI):
    def __init__(self, zipcode="92617", ccode="US"):
        self._zipcode = zipcode
        self._ccode = ccode
        self._apikey = ""
        self._response_dict = []
        self.message = ""

        super().__init__()

    def load_data(self) -> None:
      '''
      Calls the web api using the required values and stores the response in class data attributes.
            
      '''
      zipcode = self._zipcode
      ccode = self._ccode
      apikey = self._apikey
      api_call = f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={apikey}'

      weather_dict = OpenWeather.download_url(api_call)

      
      for key in weather_dict.keys():
          if key == 'main' or key == 'coord':
              inside_dict = weather_dict[key]
              
              for key2, value2 in inside_dict.items():
                  d = {key2: value2}
                  self.__dict__.update(d)
                  
    def transclude(self, message: str) -> str:
        transclude = self.transclude
        zipcode = self._zipcode
        ccode = self._ccode
        apikey = "c8247c52481199e8d1642166e7627dcc"
        open_weather = OpenWeather(zipcode, ccode)
        open_weather.set_apikey(apikey)
        open_weather.load_data()
        replace_weather = f"The temperature for {zipcode} is {open_weather.temp} degrees."
        message = message.replace("@weather", replace_weather)
        self.message = message
        return message
    
    








    
