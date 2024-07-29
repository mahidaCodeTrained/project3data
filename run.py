# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import colorama
colorama.init()
import time
import re
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('film/book_survey')

# This function is a introduction to the survey
def welcome_message():
    print(colorama.Fore.GREEN + f"Program taking shape in 5....4....3....2....1....")
    time.sleep(5)
    clear()
    print(f"Welcome to the Film and Book Survey! \n")
    time.sleep(5)
    print(f"This Survey was created to understand interests")
    print(f"of film and book enthusiasts in 2024 the survey will")
    print(f"gain information and understanding from survey answers.\n")
    time.sleep(6)
    print(f"You will be asked a few questions either about film or books")
    print(f"depending on your preference so sit tight and complete the survey!\n")
    time.sleep(6)
    clear()

"""
The clear() function has proven to be a useful idea that I took
from user "t0tacci0" from GitHub.
"""
def clear():
    # Check the OS and clear the screen
    if os.name == 'nt':  # This is for Windows
        os.system('cls')
    else:  # This is for Linux and macOS
        os.system('clear')



def starting_page():
        print(colorama.Fore.MAGENTA + f"To begin this survey we need to know if you" )
        print(f"are a moviegoer or a bookreader!")
        time.sleep(3)
    
welcome_message()
starting_page()
    
    
    
    
    
    
   
   