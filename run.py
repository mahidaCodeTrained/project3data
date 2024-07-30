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

# Global variable created so I can use user_name throughout project.
user_name = None

def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux and macOS
        os.system('clear')

def welcome_message():
    print(colorama.Fore.GREEN + "Program taking shape in 5....4....3....2....1....")
    time.sleep(5)
    clear()
    print("Welcome to the Film and Book Survey! \n")
    time.sleep(5)
    print("This Survey was created to understand interests")
    print("of film and book enthusiasts in 2024. The survey will")
    print("gain information and understanding from survey answers.\n")
    time.sleep(6)
    print("You will be asked a few questions either about film or books")
    print("depending on your preference so sit tight and complete the survey!\n")
    time.sleep(6)
    clear()

def get_user_name_age():
    global user_name
    while True:
        user_name = input(colorama.Fore.YELLOW + "Please enter your name: ")
        print()
        if re.match("^[a-zA-Z]+$", user_name):
            print(colorama.Fore.GREEN + "Thank you.")
            time.sleep(2)
            clear()
            while True:
                print(colorama.Fore.GREEN + "You must enter an age between 7-110 so that the survey")
                print(colorama.Fore.GREEN + "is reasonably conducted by people of human age.")
                user_age = input(colorama.Fore.YELLOW + "Please enter your age: ")
                print()
                if user_age.isdigit() and 7 <= int(user_age) <= 110:
                    print(colorama.Fore.GREEN + "Thank you.")
                    # Append user name and age to the "names" worksheet
                    user_name_worksheet = SHEET.worksheet("names")
                    user_name_worksheet.append_row([user_name, user_age])
                    break
                else:
                    print(colorama.Fore.RED + "Invalid age.")
                    print(colorama.Fore.RED + "You must enter a valid age (between 7-110).")
            break
        else:
            print(colorama.Fore.RED + "Invalid name.")
            print(colorama.Fore.RED + "Please enter a valid name with only letters.")
    print(colorama.Fore.GREEN + f"Hello, {user_name}! Preparing the Code Survey.\n")
    time.sleep(4)
    clear()
    return user_name

def starting_page():
    print(colorama.Fore.MAGENTA + "To begin this survey we need to know if you")
    print("are a moviegoer or a bookreader so we can tailor your experience!\n")
    time.sleep(3)
    print(colorama.Fore.MAGENTA + "1. Moviegoer")
    print(colorama.Fore.MAGENTA + "2. Bookreader")
    user_choice = input(colorama.Fore.YELLOW + "Enter your choice from option 1, or option 2: ")

    if user_choice == '1':
        film_survey()
        clear()
    elif user_choice == '2':
        book_survey()  # Placeholder for book survey function
        clear()

def film_survey():
    if user_name is None:
        print(colorama.Fore.RED + "Error: User name not set. Please start the survey again.")
        return

    print(colorama.Fore.GREEN + "The film survey will now begin!")
    time.sleep(3)
    clear()

    print(colorama.Fore.GREEN + f"Once again, welcome {user_name} we are thrilled that you have")
    print(colorama.Fore.GREEN + "taken the time to take this short survey!\n")
    time.sleep(4)
    print(colorama.Fore.GREEN + "As you have selected option 1 'Moviegoer' we have taken this into account")
    print(colorama.Fore.GREEN + "and have built a tailormade survey just for you to dive into.")
    print(colorama.Fore.GREEN + "It's now time to sit back get a drink or some popcorn and answer a few questions!")
    time.sleep(7)
    clear()

    film_data = []

    """
    Question 1
    """
    while True:
        print(colorama.Fore.YELLOW + "Question One: From these options what best describes your level")
        print(colorama.Fore.YELLOW + "of enthusiasm for films in 2024?\n")
        print(colorama.Fore.YELLOW + "1. Super Enthusiasm")
        print(colorama.Fore.YELLOW + "2. Moderate Enthusiasm")
        print(colorama.Fore.YELLOW + "3. Mild Enthusiasm")
        print(colorama.Fore.YELLOW + "4. Little Enthusiasm\n")

        film_answer = input("Please enter your answer(from '1' '2' '3' '4'): ")

        if film_answer in ['1', '2', '3', '4']:
            film_data.append(film_answer)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "You have entered an invalid answer...")
            print(colorama.Fore.RED + "Please make sure your answer corresponds to the option numbers.")
            time.sleep(2)
            clear()

    """
    Question 2
    """ 
    while True:
        print(colorama.Fore.YELLOW + "Question Two: On a scale of 1-10 how would you rate")
        print(colorama.Fore.YELLOW + "the cinema going experience in 2024 based on its enjoyableness? ")
        print(colorama.Fore.GREEN + "You must answer this question with numbers ranging from 1-10")
        print(colorama.Fore.GREEN + "(1 is least enjoyable, 10 is greatly enjoyable).")
        try:
            rating = int(input("Please enter a rating between 1-10: "))
            if 1 <= rating <= 10:
                film_data.append(str(rating))  # Convert to string for consistency
                print("We have collected this data, thank you and on to the next question!")
                time.sleep(2)
                clear()
                break
            else:
                print(colorama.Fore.RED + "Invalid rating.")
                print(colorama.Fore.RED + "Please enter a number between 1 and 10.")
                time.sleep(2)
                clear()
        except ValueError:
            print(colorama.Fore.RED + "Invalid input.")
            print(colorama.Fore.RED + "Please enter a number between 1 and 10.")
            time.sleep(2)
            clear()

    """
    Question 3
    """ 
    while True:
        print(colorama.Fore.YELLOW + f"Question Three: {user_name}, on a scale of 1-10 how often")
        print(colorama.Fore.YELLOW + "do you sit down and watch movies?")
        print(colorama.Fore.GREEN + "(1) meaning almost never, while (10) means all the time.")
        try:
            often_rating = int(input("Please enter a rating between 1-10: "))
            if 1 <= often_rating <= 10:
                film_data.append(str(often_rating))
                print("We have collected this data, thank you!")
                time.sleep(2)
                clear()
                break
            else:
                print(colorama.Fore.RED + "Invalid rating.")
                print(colorama.Fore.RED + "Please enter a number between 1 and 10.")
                time.sleep(2)
                clear()
        except ValueError:
            print(colorama.Fore.RED + "Invalid input.")
            print(colorama.Fore.RED + "Please enter a number between 1 and 10.")
            time.sleep(2)
            clear()

    # Append the film data to the Google Sheet
    film_survey_worksheet = SHEET.worksheet("film")
    film_survey_worksheet.append_row(film_data)

# Entry point of the script
welcome_message()
get_user_name_age()  # Collect the user’s name and age first
starting_page()





    
    
    
    
    
    
   
   