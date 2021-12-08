# ds_protocol.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

import json
from collections import namedtuple

def extract_json(json_msg:str):
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    StoreTuple = namedtuple('DataTuple', ['type', 'message', 'token'])
    json_obj = json.loads(json_msg)
    type_in = json_obj['response']['type']
    message_in = json_obj['response']['message']
    if 'token' in json_obj['response']:
      token = json_obj['response']['token']
      
      return StoreTuple(type_in, message_in, token)
    else:
      print(json_obj['response']['message'])
  except json.JSONDecodeError:
    print("Json cannot be decoded.")




def join(username, password, public_key):
  joindict = '{{"join": {{"username": "{}","password": "{}", "token":"{}"}}}}'.format(username,password, public_key)
  return joindict

def post(token, message):
  postdict = '{{"token":"{}", "post": {{"entry": "{}","timestamp": "1603167689.3928561"}}}}'.format(token, message)
  return postdict

def bio(token, bio):
  biodict = '{{"token":"{}", "bio": {{"entry": "{}", "timestamp": "16031167689.3928561"}}}}'.format(token, bio)
  return biodict

  
