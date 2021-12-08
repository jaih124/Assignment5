# input_processor.py

# Jai Hathiramani
# jhathira@uci.edu
# 29936257

def run_command_inputs():
    og_input = input("Enter Input: ")
    return og_input

def create_profile_inputs():
    new_username = input("Username: ")
    new_password = input("Password: ")
    new_bio = input("Bio: ")

    return (new_username, new_password, new_bio)

def welcome_input():
    user_welcome_input = input("Welcome! Do you want to create or load a DSU file? If you would like to post to a DS server, you must create a new profile. (type 'C' to create or 'O' to open): ")
    return user_welcome_input
