# ds_client.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

import socket
import ds_protocol
#from NaClProfile import NaClProfile
from NaClDSEncoder import NaClDSEncoder
from Profile import Profile, Post

def send(server:str, port:int, username:str, password:str, message:str, bio:str, public_key='vdirk5LGbhw2IVI+91PONapH1xHRaGd2gtIHRzZ+iwU=', private_key='ZwNTt5L2KJ03vZharPPxchWfRXrW0ldoiuS0hWjqLCc='):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server,port))

    send = client.makefile('w')
    recv = client.makefile('r')

    join_ = ds_protocol.join(username, password, public_key)
    send.write(join_ + '\r\n')
    send.flush()
    srv_msg = recv.readline()
    
    token1 = ds_protocol.extract_json(srv_msg)
    print(token1)

    my_key = NaClProfile()
    my_key.private_key = private_key
    encrypted_message = (my_key.encrypt_entry(token1.token, message).decode('utf-8'))
       
    post_variable = Post(message)
    post_ = ds_protocol.post(public_key,encrypted_message)
    send.write(post_ + '\r\n')
    send.flush()
    srv_msg = recv_readlines()
    
    token2 = ds_protocol.extract_json(srv_msg)

    encrypted_bio = (my_key.encrypt_entry(bio, token1.token).decode('utf-8'))
    bio_ = ds_protocol.bio(public_key,encrypted_bio)
    send.write(bio_ + '\r\n')
    send.flush()
    srv_msg = recv.readline()

  


  

