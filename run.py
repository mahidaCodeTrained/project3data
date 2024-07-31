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

"""
The function "get_user_name_age" is designed to gather the users name and age
through input. The user's input will then be delivered to a sheet called 'names'
through appending the data.
"""

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

"""
The function "starting_page" is designed to introduce the survey and the two different
tailored options that users can go about taking the survey. In either a moviergoer or 
bookreader survey. The function is designed to transport the user to different functions depending
on their answer to the question.
"""   

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

"""
The film_survey function is designed for users who chose the "Moviergoer" option in the starting_page function
This function is tailored with questions regarding film and the data provided by the user
is collected and stored in a sheet named 'film' through appending the data in rows.
"""
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
    bonus_data = []

    # Question 1
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

    # Question 2
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

    # Bonus Question 1
    while True:
        print(colorama.Fore.CYAN + "Bonus Question One: Do you purchase snacks and drinks at the cinema?\n")
        print(colorama.Fore.CYAN + "1. Yes")
        print(colorama.Fore.CYAN + "2. No\n")

        print("Your answer must be either the numbers (1) or (2)")
        bonus_snack = input("Please enter an answer now: ")
        if bonus_snack in ['1', '2']:
            bonus_data.append(bonus_snack)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(4)
            clear()
            break
        else:
            print(colorama.Fore.RED + "The answer you have submitted is invalid.")
            print(colorama.Fore.RED + "Please submit a number, either '1' or '2' depending on your preference.")

    # Question 3
    while True:
        print(colorama.Fore.YELLOW + f"Question Three: {user_name}, on a scale of 1-10 how often")
        print(colorama.Fore.YELLOW + "do you sit down and watch movies?")
        print(colorama.Fore.GREEN + "(1) meaning almost never, while (10) means all the time.")
        try:
            often_rating = int(input("Please enter a rating between 1-10: "))
            if 1 <= often_rating <= 10:
                film_data.append(str(often_rating))
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

    # Question 4
    while True:
        print(colorama.Fore.YELLOW + "Question Four: Have you been to the cinema in the past month?\n ")
        print(colorama.Fore.GREEN + "You must select either (1) or (2) for 'Yes' or 'No'")
        print(colorama.Fore.YELLOW + "1. Yes")
        print(colorama.Fore.YELLOW + "2. No")

        cinema = input("Please submit your answer now: ")

        if cinema in ['1', '2']:
            film_data.append(cinema)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(3)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid.")
            print(colorama.Fore.RED + "Please enter the number either ('1') or ('2') depending on your choice..")
            time.sleep(3)
            clear()

    # Bonus Question 2
    while True:
        print(colorama.Fore.CYAN + "Bonus Question Two: What day do you usually go to the cinema?")
        print(colorama.Fore.CYAN + "1. Monday")
        print(colorama.Fore.CYAN + "2. Tuesday")
        print(colorama.Fore.CYAN + "3. Wednesday")
        print(colorama.Fore.CYAN + "4. Thursday")
        print(colorama.Fore.CYAN + "5. Friday")
        print(colorama.Fore.CYAN + "6. Saturday")
        print(colorama.Fore.CYAN + "7. Sunday")

        day_cinema = input("Please submit your answer now: ")

        if day_cinema in ['1', '2', '3', '4', '5', '6', '7']:
            bonus_data.append(day_cinema)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(4)
            clear()
            break
        else:
            print(colorama.Fore.RED + "The answer you have submitted is invalid.")
            print(colorama.Fore.RED + "Please submit a number, between '1' or '7' depending on your preference.")
            time.sleep(2)
            clear()

    # Question 5
    while True:
        print(colorama.Fore.YELLOW + "Question Five: From this selection what is your favourite genre of film\n ")
        print(colorama.Fore.YELLOW + "1. Action")
        print(colorama.Fore.YELLOW + "2. Drama")
        print(colorama.Fore.YELLOW + "3. Crime/Thriller")
        print(colorama.Fore.YELLOW + "4. Romance")
        print(colorama.Fore.YELLOW + "5. Comedy")
        print(colorama.Fore.YELLOW + "6. Sci-Fi")
        print(colorama.Fore.YELLOW + "7. Other\n")
        print(colorama.Fore.GREEN + "In this question you must select an answer between the numbers 1 and 7 depending on your preference.\n")
        genre = input("Please select an option now: ")

        if genre in ['1', '2', '3', '4', '5', '6', '7']:
            film_data.append(genre)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(4)
            clear()
            break
        else:
            print(colorama.Fore.RED + "Sorry but this entry is invalid.")
            print(colorama.Fore.RED + "You must select a number from 1-7")
            time.sleep(3)
            clear()

    # Bonus Question 3
    if genre == '1':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite action movie?")
    elif genre == '2':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite drama movie?")
    elif genre == '3':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite crime movie?")
    elif genre == '4':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite romance movie?")
    elif genre == '5':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite comedy movie?")
    elif genre == '6':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite Sci-Fi movie?")
    elif genre == '7':
        print(colorama.Fore.CYAN + "Bonus Question Three: I see that you have selected 'Other'\
 I'll simply ask what is your all-time favorite movie?\n")
    
    favorite = input("Please enter your answer: ")
    bonus_data.append(favorite)

    print(colorama.Fore.CYAN + f"Thank you for answering {user_name}, on to the final question!")
    time.sleep(4)
    clear()
  
    

    while True:
        print(colorama.Fore.YELLOW + "Question Six: When will you watch your next movie?\n")
        print(colorama.Fore.YELLOW + "1. Today")
        print(colorama.Fore.YELLOW + "2. This Week")
        print(colorama.Fore.YELLOW + "3. This Month")
        print(colorama.Fore.YELLOW + "4. This Year")

        watch_movie = input("Please enter your answer now: ")
        if watch_movie in ['1', '2', '3', '4']:
            film_data.append(watch_movie)
            print(f"Thank you for answering {user_name}.")
            time.sleep(4)
            clear()
            break 
        else:
            print(colorama.Fore.RED +"Sorry but this answer is invalid.")
            print(colorama.Fore.RED + "Please enter a value between [1-4]")
            time.sleep(3)
            clear()

    # Append data to Google Sheets
    try:
        film_survey_worksheet = SHEET.worksheet("film")
        film_survey_worksheet.append_row(film_data)
        bonus_survey_worksheet = SHEET.worksheet("bonus")
        bonus_survey_worksheet.append_row(bonus_data)
    except Exception as e:
        print(colorama.Fore.RED + "An error occurred while appending the data to Google Sheets:")
        print(colorama.Fore.RED + str(e))



    print("Calling end_survey_film() now...")  # Debugging statement
    end_survey_film()  # Call the end_survey_film function here to conclude the survey

def end_survey_film():
    clear()
    print(f"Thank you for taking this film survey, {user_name}!")
    print("This survey and the data recorded will help us understand")
    print("the mindset of a film enthusiast in 2024.\n")
    
    print("I'm sure you're keen to know just how everybody who has completed")
    print("this survey has gotten on, so please select the option to 'View Statistics'.\n")
    print("However, if you want to just exit the program then please select 'Exit'.\n")
    
    print("1. View Statistics")
    print("2. Exit")

    while True:
        choice = input("Where would you like to go (1) or (2)? ")
        if choice == '1':
            view_statistics()
            break
        elif choice == '2':
            print(colorama.Fore.GREEN + "Exiting the Survey")
            print("Thank you for your time!")
            time.sleep(2)
            print("Your data submitted in this survey will be stored.")
            print("May we meet again in another survey!")
            time.sleep(3)
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, that is invalid.")
            print("Please enter the number (1) or (2).")


"""
This function book_survey was created for users who selected Option 2
"Bookreaders" in the entry question in this project. It has questions tailor-made 
so that bookreaders can honestly complete it.
"""

def book_survey():
    if user_name is None:
        print(colorama.Fore.RED + "Error: User name not set. Please start the survey again.")
        return

    print(colorama.Fore.GREEN + "The book survey will now begin!")
    time.sleep(3)
    clear()

    print(colorama.Fore.GREEN + f"Once again, welcome {user_name}, we are thrilled that you have")
    print(colorama.Fore.GREEN + "taken the time to take this short survey!\n")
    time.sleep(4)
    print(colorama.Fore.GREEN + "As you have selected option 2 'Bookreader' we have taken this into account")
    print(colorama.Fore.GREEN + "and have built a tailor-made survey just for you to dive into.")
    print(colorama.Fore.GREEN + "It's now time to sit back, get a drink or some popcorn, and answer a few questions!")
    time.sleep(7)
    clear()

    book_data = []
    bonus_book_data = []

    # Question 1
    while True:
        print(colorama.Fore.YELLOW + "Question One: From a scale of 1-10 please tell me how")
        print(colorama.Fore.YELLOW + "often you read books\n")
        print(colorama.Fore.GREEN + "You must answer this question with numbers ranging from 1-10")
        print(colorama.Fore.GREEN + "(1 is extremely rarely, 10 is all the time).")
        try:
            often_read = int(input("Please enter a rating between 1-10: "))
            if 1 <= often_read <= 10:
                book_data.append(str(often_read))  # Convert to string for consistency
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

    # Bonus Book Question 1
    while True:
        print(colorama.Fore.CYAN + "Bonus Question One: Have you ever been to a book convention?\n")
        print(colorama.Fore.CYAN + "1. Yes")
        print(colorama.Fore.CYAN + "2. No\n")
        print(colorama.Fore.GREEN + "You must answer this question with the numbers (1) or (2).")

        convention = input("Please enter your answer: ")
        if convention in ['1', '2']:
            bonus_book_data.append(convention)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(3)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid.")
            print("You must answer with the numbers (1) or (2).")
            time.sleep(3)
            clear()

    # Question 2
    while True:
        print(colorama.Fore.YELLOW + "Question Two: What type of books do you read/view?\n")
        print(colorama.Fore.YELLOW + "1. Physical Books")
        print(colorama.Fore.YELLOW + "2. E-books")
        print(colorama.Fore.YELLOW + "3. Audiobooks")
        print(colorama.Fore.GREEN + "You must enter a value between (1-3) based on your preference.")

        book_type = input("Please enter your answer now: ")
        if book_type in ['1', '2', '3']:
            book_data.append(book_type)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(3)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between the numbers (1-3)")
            time.sleep(4)
            clear()

    # Question 3
    while True:
        print(colorama.Fore.YELLOW + "Question Three: When you purchase a book how important is the")
        print(colorama.Fore.YELLOW + "cover-art in the psychology of making your purchase\n")
        print(colorama.Fore.YELLOW + "1. Very Important")
        print(colorama.Fore.YELLOW + "2. Somewhat Important")
        print(colorama.Fore.YELLOW + "3. Not Very Important")
        print(colorama.Fore.YELLOW + "4. Not at all Important\n")
        print(colorama.Fore.GREEN + "You must enter a value between (1-4) based on your preference.")

        cover_art = input("Please enter your answer now: ")
        if cover_art in ['1', '2', '3', '4']:
            book_data.append(cover_art)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(3)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between the numbers (1-4)")
            time.sleep(4)
            clear()

    # Bonus Question Two
    while True:
        print(colorama.Fore.CYAN + "Bonus Question Two: What type of book-cover attracts your eye?\n")
        print(colorama.Fore.CYAN + "1. Colorful")
        print(colorama.Fore.CYAN + "2. Interesting Picture")
        print(colorama.Fore.CYAN + "3. Material")
        print(colorama.Fore.CYAN + "4. Comments on Cover")

        print(colorama.Fore.GREEN + "Please select an option through (1-4) using the numbers (1-4)")
        attract = input("Please submit your answer: ")
        if attract in ['1', '2', '3', '4']:
            bonus_book_data.append(attract)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(4)
            clear()

            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between the numbers (1-4)")
            time.sleep(4)
            clear()

    # Question 4
    while True:
        print(colorama.Fore.YELLOW + "Question Four: Roughly, how many hours do you spend reading")
        print(colorama.Fore.YELLOW + "a book at once during one book-reading session?\n")
        print(colorama.Fore.YELLOW + "1. Under an hour")
        print(colorama.Fore.YELLOW + "2. 1-2 hours")
        print(colorama.Fore.YELLOW + "3. 2-4 hours")
        print(colorama.Fore.YELLOW + "4. Over 4 hours")

        read_hours = input("Please submit your answer: ")
        if read_hours in ['1', '2', '3', '4']:
            book_data.append(read_hours)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(4)
            clear()

            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between the numbers (1-4)")
            time.sleep(4)
            clear()

    
    # Question 5
    while True:
        print(colorama.Fore.YELLOW + "Question Five: From these options please tell us what is your favourite\
 genre of book?\n")
        print(colorama.Fore.YELLOW + "1. Fantasy")
        print(colorama.Fore.YELLOW + "2. Dystopian")
        print(colorama.Fore.YELLOW + "3. Romance Novel")
        print(colorama.Fore.YELLOW + "4. Horror")
        print(colorama.Fore.YELLOW + "5. Biography")
        print(colorama.Fore.YELLOW + "6. Historical Fiction")
        print(colorama.Fore.YELLOW + "7. Science Fiction")
        print(colorama.Fore.YELLOW + "8. Humour")
        print(colorama.Fore.YELLOW + "9. Childrens")
        print(colorama.Fore.YELLOW + "10. Mystery")

        fav_book = input("Please submit your answer:")
        if fav_book in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            book_data.append(fav_book)
            print("We have collected this data, thank you and on to the next question!")
            time.sleep(3)
            clear()

            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between the numbers (1-10)")
            time.sleep(4)
            clear()
   
    # Bonus Question 3
    if fav-book == '1':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite fantasy book?")
    elif fav-book == '2':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite dystopian novel?")
    elif fav-book == '3':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite romance Novel?")
    elif fav_book == '4':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite horror book?")
    elif fav-book == '5':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite biography?")
    elif fav_book == '6':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all-time favorite historical fiction novel?")
    elif fav-book == '7':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all time favourite science fiction novel?\n")
    elif fav-book == '8':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all time favourite humour novel?\n")
    elif fav-book == '9':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all time favourite childrens book?\n")
    elif fav-book == '10':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your all time favourite Mystery novel?\n")

        fav_book = input("Please enter your answer: ")
    bonus_book_data.append(fav_book)

    print(colorama.Fore.CYAN + f"Thank you for answering {user_name}, on to the final question!")
    time.sleep(4)
    clear()


    # Question 6
    while True:
        print(colorama.Fore.YELLOW + "Question Six: When will you read your next book?\n")
        print(colorama.Fore.YELLOW + "1. Today")
        print(colorama.Fore.YELLOW + "2. This Week")
        print(colorama.Fore.YELLOW + "3. This Month")
        print(colorama.Fore.YELLOW + "4. This Year")

        reading = input("Please enter your answer now: ")
        if reading in ['1', '2', '3', '4']:
            book_data.append(reading)
            print(f"Thank you for answering {user_name}.")
            time.sleep(4)
            clear()
            break 
        else:
            print(colorama.Fore.RED +"Sorry but this answer is invalid.")
            print(colorama.Fore.RED + "Please enter a value between [1-4]")
            time.sleep(3)
            clear()


        

    # This allows for the data to append to Google Sheets
    try:
        book_survey_worksheet = SHEET.worksheet('book')
        book_survey_worksheet.append_row(book_data)
        bonus_book_survey_worksheet = SHEET.worksheet('bookbonus')
        bonus_book_survey_worksheet.append_row(bonus_book_data)
        print(colorama.Fore.GREEN + "Book survey data has been successfully recorded.")
    except Exception as e:
        print(colorama.Fore.RED + "An error occurred while appending the data to Google Sheets:")
        print(colorama.Fore.RED + str(e))


        end_survey_book()

def end_survey_book():
    clear()




# Entry point of the script
welcome_message()
get_user_name_age()  # Collect the user’s name and age first
starting_page()





    
    
    
    
    
    
   
   