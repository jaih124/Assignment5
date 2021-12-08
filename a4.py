# a4.py


# Jai Hathiramani
# jhathira@uci.edu
# 29936257

import Profile
from pathlib import Path
import os
from os.path import exists
import json
import input_processor
import ds_client
import OpenWeather
import LastFM
import WebAPI
import NaClProfile

def run():
 
    #A1 & A2 & A3 & A4 Processing
    welcome_message_ = welcome_message() #display welcome message (Load or Create)

    while True:
        og_input = input_processor.run_command_inputs()
        user_input = og_input.split()
        

        if os.path.exists(user_input[1]) or user_input[0] in ['E','P']: # choose either L, Q, D, C, R
            if user_input[0] in ['L', 'C']:
                user_path_location = list_files(user_input[1])
            if user_input[0] in ['D', 'R', 'O', 'E', 'P']:
                file_delete = user_input[1]
                read_file = user_input[1]
                user_path_location = user_input[1]

                
            if len(user_input) == 2:
                if user_input[0] == 'L': 
                    for i in user_path_location:
                        print(i)
            if user_input[0] == 'C' and user_input[2] == '-n': #create file and name the file you want to create
                filename = user_input[3]
                new_file = create_file(user_path_location[1], filename)
                print(user_input[1], end='')
                dsu_path = '/' + filename + ".dsu"
                print('\\' + filename + ".dsu")
                new_profile = create_profile(os.path.abspath(filename+".dsu"))
                old_file_name = filename + '.dsu'

                load_path = user_input[1] + '\\' + filename + ".dsu"

                #load profile objects and store them for send function 
                x = Profile.Profile()
                x.load_profile(load_path)

                senduser = x.username
                sendpwd = x.password
                sendbio = x.bio
                
                
            #user interface for A3
            #asks user if you would like to send information to a server
                server_call = input("Would you like to send this to a server? If yes type in Y. If no type in N ")

                if server_call == "Y":
                    print("Please Note: '@weather' displays the current temperature for a user-specified zipcode.")
                    print("Please Note: '@lastfm' displays the current top track for a user-specified artist")
                    message = input("What message would you like to post")
                    # a4 using API data within message
                    if "@weather" in message:
                    
                        zipcode = input("Enter ZIP Code within US: ")
                        ccode = "US"
                        openweather_object = OpenWeather.OpenWeather(zipcode,ccode)
                        openweather_object.transclude(message)
                        message= openweather_object.message

                    if "@lastfm" in message:
                    
                        artist = input("Enter Artist Name. You must use '+' to replace spaces within the name: ")
                        lastfm_object = LastFM.LastFM(artist)
                        lastfm_object.transclude(message)
                        message = lastfm_object.message

                    #asks user for server name to post and utilizes send function to post message
                    server_name = input("Enter Server Address")
                    ds_client.send(server_name, 3021, senduser, sendpwd, message, sendbio, public_key='vdirk5LGbhw2IVI+91PONapH1xHRaGd2gtIHRzZ+iwU=', private_key='ZwNTt5L2KJ03vZharPPxchWfRXrW0ldoiuS0hWjqLCc=')
                    theclass = NaClProfile
                    theclass.add_post(message)
                if server_call == "N":
                    print("Restart Program to Run Again. All functionality from A1 & A2 still in place. You may use those commands.")


            # deletes file
            if user_input[0] == "D" and str(file_delete).endswith('.dsu') and file_delete.is_file():
                path_to_file_name = user_input[1]
                Path(path_to_file_name).unlink()
                print(path_to_file_name + " DELETED")


            if len(user_input) == 2:
                if user_input[0] == "R":
                    with open(read_file.rsplit('/', 1)[-1]) as f:
                        lines_in_file = f.readlines()

                        if lines_in_file:
                            for line in lines_in_file:
                                print(line)
                        else:
                            print('EMPTY')

            #opens file location and loads profile
            if user_input[0] == 'O':
                dsu_load_path = user_path_location
                profile_ = Profile.Profile()
                old_file_name = os.path.basename(Path(dsu_load_path))
                try:
                    profile_ = profile_.load_profile(dsu_load_path)
                    print("Profile loaded successfully.")
                except:
                    print("Profile has not been loaded.")
                
            # formatting for printing user information 
            if user_input[0] == 'E':
                edit_list = og_input
                
                with open(old_file_name, 'r+') as f:
                    json_dict = json.load(f)
                        
                for i in range(len(edit_list)):
                    
                    # formats user-specified username, password, bio, 
                    if edit_list[i:i+4] == "-usr":
                        sliced_string = edit_list[i+6:]
                        username = sliced_string[:sliced_string.index('"')]
                        json_dict['username'] = username
                    if edit_list[i:i+4] == "-pwd":
                        sliced_string = edit_list[i+6:]
                        password = sliced_string[:sliced_string.index('"')]
                        json_dict['password'] = password
                        
                    if edit_list[i:i+4] == "-bio":
                        sliced_string = edit_list[i+6:]
                        bio = sliced_string[:sliced_string.index('"')]
                        json_dict['bio'] = bio

                    # appends profile created with add post or delete post
                    if edit_list[i:i+8] == "-addpost":
                        sliced_string = edit_list[i+10:]
                        addpost = sliced_string[:sliced_string.index('"')]
                        
                        json_dict['_posts'].append(Profile.Post(addpost))

                    if edit_list[i:i+8] == "-delpost":
                        slice_string = edit_list[i:]
                        delpost_split = slice_string.split()
                        delpost_index = delpost_split[1]

                        del_index = int(delpost_index)
                        json_dict['_posts'].pop(del_index)

                 
                os.remove(old_file_name)
                with open(old_file_name, 'w') as f:
                    json.dump(json_dict, f, indent=4)

            #lists user-specificed username, password, bio, posts, and all
            if user_input[0] == 'P':
                command = user_input[1]
                with open(old_file_name, 'r') as f:
                    json_dict = json.load(f)
                    
                if command == "-usr":
                    print(json_dict['username'])
                if command == "-pwd":
                    print(json_dict['password'])
                        
                if command == "-bio":
                    print(json_dict['bio'])

                if command == "-posts":
                    for post in json_dict['_posts']:
                        print(post, "ID:", json_dict['_posts'].index(post))

                if command == "-post":
                    id_ = user_input[2]
                    id_ = int(id_[1:len(id_)-1])

                    print(json_dict['_posts'][id_])
                    
 
                if command == "-all":
                    print(json_dict)

            #quits program       
            if user_input[0] == 'Q':
                quit()
            


            if len(user_input) >= 3 and "-r" in user_input:  
                user_path_location = directory_content_recursively(user_input[1])

                if '-r' and '-f' in user_input:
                    for i in user_path_location:
                        if Path(i).is_file():
                            print(i)
                elif "-r" and "-e" in user_input:
                    extension_list = search_extension(user_path_location,user_input[-1])
                    for i in extension_list:
                        print(i)
                else:
                    for i in user_path_location:
                        print(i)
            

            if len(user_input) >= 3 and user_input[2] == "-s":

                input_files = file_only(user_path_location, user_input[3])
            
                for i in input_files:

                    print(i)

            if len(user_input) >= 3 and '-f' in user_input:
                user_path_location = files_no_direct(user_input[1])
                for i in user_path_location:
                    if Path(i).is_file():
                        print(i)

            if len(user_input) >= 3 and "-e" in user_input and "-r" not in user_input:
                extension_list = search_extension(user_path_location, user_input[-1])
                for i in extension_list:
                    print(i)
                    
        else:
            print('ERROR')


#DIRECTORY FUNCTIONS

# create user file
def create_file(path, filename):
    f = open(filename + '.dsu', "w+")
    
# deletes file
def delete_File(path_filename):
    f = file_path.unlink()

#lists all files win the path
def list_files(the_path):
    res = list()
    list_dir = os.listdir(Path(the_path))
    
    for f in list_dir:
        user_path_location = Path(the_path) / f
        if user_path_location.is_file():
            res.append(user_path_location)
     
    res.sort()

    for f in list_dir:
        user_path_location = Path(the_path) / f
        if user_path_location.is_dir():
           res.append(user_path_location)
            
    return res
   

def directory_content_recursively(the_path):
    '''-r directory, outputs directory content recursively'''
   
    the_path = Path(the_path)
    list_dir = os.listdir(the_path)
    recursive_result = []  
    list_files = []
    list_dir.sort()
    
   
    for f in list_dir:
        user_path_location = the_path / f
        if user_path_location.is_dir():
            recursive_result.append(user_path_location)
            recursive_result = recursive_result + directory_content_recursively(str(user_path_location))
        if user_path_location.is_file():
            list_files.append(user_path_location)

           
    recursive_result.sort()
    list_files.sort()
    
   
    return list_files + recursive_result

def files_no_direct(the_path):
    '''-f directory, outputs only files, excluding directories in the results'''
   
    the_path = Path(the_path)
    list_dir = os.listdir(the_path)
    directory_final = list()
   
    for f in list_dir:
        user_path = the_path / f
        if user_path.is_file():
            directory_final.append(user_path)

    directory_final.sort()      
       
    return directory_final
   

def file_only(the_path_list, file_name):
    '''-s directory, outputs only files that match a given file name'''
    file_list = list()
    dir_list = list()
    
    for p in the_path_list:
        if p.is_file():
            if p.name == file_name:
                file_list.append(path_input)
        if p.is_dir():
            for i in p.iterdir():
                dir_name.append(i)
  
    if dir_list != []:
        search_for_files = file_only(dir_list, name)
        file_list.extend(search_for_files)
        
    return file_list

def search_extension(the_path, extension):
    '''-e directory, outputs only files that match a given file extension'''
    extension_final = list()
    dir_extension_list = list()
              
    for user_path_location in the_path:
        if user_path_location.is_file():
            if str(path_input).endswith(extension):
                extension_final.append(path_input)
   
        if user_path_location.is_dir():
            for ele in user_path_location.iterdir():
                dir_extension_list.append(ele)


    return extension_final

# create user profile
def create_profile(the_path):
    new_username, new_password, new_bio = input_processor.create_profile_inputs()
    dsuserver = ""
    
    profile_ = Profile.Profile()
    profile_.dsuserver = dsuserver
    profile_.bio = new_bio
    profile_.username = new_username
    profile_.password = new_password

    profile_.save_profile(the_path)
    
# welcome message function
def welcome_message():
    user_welcome_input = input_processor.welcome_input()
    if user_welcome_input.lower() != "admin":
        if user_welcome_input == 'C':
            print("To create enter:")
            print("C C/path/to/your/file -n YOUR_FILE_NAME")
        if user_welcome_input == 'O':
            print("To open enter:")
            print("O /path/to/your/file/YOUR_FILE_NAME.dsu")
         
run()



