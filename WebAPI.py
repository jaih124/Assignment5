# WebAPI.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

from abc import ABC, abstractmethod
import urllib, json
from urllib import request,error

class WebAPI(ABC):
    
  def __init__(self):
     super().__init__()
     
  def download_url(url_to_download: str) -> dict:
    #TODO: Implement web api request code in a way that supports ALL types of web APIs
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))

        finally:
            if response != None:
                response.close()
    
        return r_obj
	
  def set_apikey(self, apikey:str) -> None:
      self._apikey = apikey
	
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
