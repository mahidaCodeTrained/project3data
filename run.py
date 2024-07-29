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

"""
The function get_user_name is called before starting_page function
to ensure that this is shown in the terminal ahead of it.
"""
def get_user_name():
    while True:
        user_name = input(colorama.Fore.YELLOW + "Please enter your name:")
        print()
        if re.match("^[a-zA-Z]+$", user_name):
            # Append user name to the "names" worksheet
            user_name_worksheet = SHEET.worksheet("names")
            user_name_worksheet.append_row([user_name])
            break
        else:
            print(colorama.Fore.RED + f"Invalid name.")
            print(colorama.Fore.RED + f"Please enter a valid name with only letters.")
    print(colorama.Fore.GREEN + f"Hello, {user_name}! Preparing the Code Survey.\n")


def starting_page():
    print(colorama.Fore.MAGENTA + f"To begin this survey we need to know if you" )
    print(f"are a moviegoer or a bookreader so we can tailor your experience!\n")
    time.sleep(3)
    print(colorama.Fore.MAGENTA + f"1. Moviegoer") 
    print(colorama.Fore.MAGENTA + f"2. Bookreader")
    user_choice = input(colorama.Fore.YELLOW + f"Enter your choice from option 1, or option 2")

    if user_choice == '1':
        film_survey() # This is placeholder for a function for the film survey.





welcome_message()
get_user_name()
starting_page()

    
    
    
    
    
    
   
   