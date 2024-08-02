from google.oauth2.service_account import Credentials
import gspread
import time
import re
import os
import colorama
colorama.init()

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
user_choice = None


def clear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux and macOS
        os.system('clear')


def welcome_message():
    print(colorama.Fore.GREEN + "Program Activated!")
    time.sleep(3)
    clear()
    print("Welcome to the Film and Book Survey! \n")
    time.sleep(3)
    print("This Survey was created to understand interests")
    print("of film and book enthusiasts in 2024. The survey will")
    print("gain information and understanding from survey answers.\n")
    time.sleep(5)
    print("You will be asked a few questions either about film or books")
    print("depending on your preference so sit tight\
 and complete the survey!\n")
    time.sleep(5)
    clear()


"""
The function "get_user_name_age" is designed to gather the users name and age
through input. The user's input will then be \
delivered to a sheet called 'names'
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
                print(colorama.Fore.GREEN + "You must enter an age between\
 7-110 so that the survey")
                print(colorama.Fore.GREEN + "is reasonably conducted by people\
 of human age.")
                user_age = input(colorama.Fore.YELLOW + "Please enter your\
 age: ")
                print()
                if user_age.isdigit() and 7 <= int(user_age) <= 110:
                    print(colorama.Fore.GREEN + "Thank you.")
                    # Append user name and age to the "names" worksheet
                    user_name_worksheet = SHEET.worksheet("names")
                    user_name_worksheet.append_row([user_name, int(user_age)])
                    break
                else:
                    print(colorama.Fore.RED + "Invalid age.")
                    print(colorama.Fore.RED + "You must enter a valid age\
 (between 7-110).")
            break
        else:
            print(colorama.Fore.RED + "Invalid name.")
            print(colorama.Fore.RED + "Please enter a valid name with only\
 letters.")
    print(colorama.Fore.GREEN + f"Hello, {user_name}!\
 Preparing the Code Survey.\n")
    time.sleep(4)
    clear()
    return user_name


"""
The function "starting_page" is designed to introduce
the survey and the two different
tailored options that users can go about taking the survey.
In either a moviergoer or
bookreader survey. The function is designed to transport the user
to different functions depending
on their answer to the question.
"""


def starting_page():
    print(colorama.Fore.GREEN + "To begin this survey we need to know if you")
    print("are a moviegoer or a bookreader so we can tailor\
 your experience!\n")
    time.sleep(3)
    print(colorama.Fore.YELLOW + "1. Moviegoer")
    print(colorama.Fore.YELLOW + "2. Bookreader")

    while True:
        user_choice = input(colorama.Fore.YELLOW + "Enter your choice\
 from option 1, or option 2: ")

        if user_choice == '1':
            film_survey()
            clear()
            break
        elif user_choice == '2':
            book_survey()
            clear()
            break
        else:
            print(colorama.Fore.RED + "Invalid choice. Please enter\
 either 1 or 2.")


"""
The film_survey function is designed for users who chose the
"Moviergoer" option in the starting_page function
This function is tailored with questions regarding film
and the data provided by the user
is collected and stored in a sheet named 'film' through
appending the data in rows.
"""


def film_survey():
    if user_name is None:
        print(colorama.Fore.RED + "Error: User name not set.\
 Please start the survey again.")
        return

    print(colorama.Fore.GREEN + "The film survey will now begin!")
    time.sleep(3)
    clear()

    print(colorama.Fore.GREEN + f"Once again, welcome {user_name}\
 we are thrilled that you have")
    print(colorama.Fore.GREEN + "taken the time to take this short survey!\n")
    time.sleep(4)
    print(colorama.Fore.GREEN + "As you have selected option 1 'Moviegoer'\
 we have taken this into account")
    print(colorama.Fore.GREEN + "and have built a tailormade survey\
 just for you to dive into.")
    print(colorama.Fore.GREEN + "It's now time to sit back get a drink\
 or some popcorn and answer a few questions!")
    time.sleep(7)
    clear()

    film_data = []
    bonus_data = []

    # Question 1
    while True:
        print(colorama.Fore.YELLOW + "Question One: From these options what\
 best describes your level")
        print(colorama.Fore.YELLOW + "of enthusiasm for films in 2024?\n")
        print(colorama.Fore.YELLOW + "1. Super Enthusiasm")
        print(colorama.Fore.YELLOW + "2. Moderate Enthusiasm")
        print(colorama.Fore.YELLOW + "3. Mild Enthusiasm")
        print(colorama.Fore.YELLOW + "4. Little Enthusiasm\n")

        film_answer = input("Please enter your answer(from '1' '2' '3' '4'): ")

        if film_answer in ['1', '2', '3', '4']:
            film_data.append(film_answer)
            print(colorama.Fore.GREEN + "We have collected this data, thank\
 you and on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "You have entered an invalid answer...")
            print(colorama.Fore.RED + "Please make sure your answer\
 corresponds to the option numbers.")
            time.sleep(2)
            clear()

    # Question 2
    while True:
        print(colorama.Fore.YELLOW + "Question Two: On a scale\
 of 1-10 how would you rate")
        print(colorama.Fore.YELLOW + "the cinema going experience\
 in 2024 based on its enjoyableness? ")
        print(colorama.Fore.GREEN + "You must answer this question\
 with numbers ranging from 1-10")
        print(colorama.Fore.GREEN + "(1 is least enjoyable,\
 10 is greatly enjoyable).")
        try:
            rating = int(input("Please enter a rating between 1-10: "))
            if 1 <= rating <= 10:
                film_data.append(str(rating))
                print("We have collected this data,\
 thank you and on to the next question!")
                time.sleep(2)
                clear()
                break
            else:
                print(colorama.Fore.RED + "Invalid rating.")
                print(colorama.Fore.RED + "Please enter a number\
 between 1 and 10.")
                time.sleep(2)
                clear()
        except ValueError:
            print(colorama.Fore.RED + "Invalid input.")
            print(colorama.Fore.RED + "Please enter a number\
 between 1 and 10.")
            time.sleep(2)
            clear()

    # Bonus Question 1
    while True:
        print(colorama.Fore.CYAN + "Bonus Question One: Do you purchase \
 snacks and drinks at the cinema?\n")
        print(colorama.Fore.CYAN + "1. Yes")
        print(colorama.Fore.CYAN + "2. No\n")

        print("Your answer must be either the numbers (1) or (2)")
        bonus_snack = input("Please enter an answer now: ")
        if bonus_snack in ['1', '2']:
            bonus_data.append(int(bonus_snack))
            print("We have collected this data, thank you and on to the \
 next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "The answer you have\
 submitted is invalid.")
            print(colorama.Fore.RED + "Please submit a number,\
 either '1' or '2' depending on your preference.")

    # Question 3
    while True:
        print(colorama.Fore.YELLOW + f"Question Three: {user_name},\
 on a scale of 1-10 how often")
        print(colorama.Fore.YELLOW + "do you sit down and watch movies?")
        print(colorama.Fore.GREEN + "(1) meaning almost never,\
 while (10) means all the time.")
        try:
            often_rating = int(input("Please enter a rating between 1-10: "))
            if 1 <= often_rating <= 10:
                film_data.append(str(often_rating))
                print("We have collected this data, thank you\
 and on to the next question!")
                time.sleep(2)
                clear()
                break
            else:
                print(colorama.Fore.RED + "Invalid rating.")
                print(colorama.Fore.RED + "Please enter a number between\
 1 and 10.")
                time.sleep(2)
                clear()
        except ValueError:
            print(colorama.Fore.RED + "Invalid input.")
            print(colorama.Fore.RED + "Please enter a number\
 between 1 and 10.")
            time.sleep(2)
            clear()

    # Question 4
    while True:
        print(colorama.Fore.YELLOW + "Question Four: Have you been to the\
 cinema in the past month?\n ")
        print(colorama.Fore.GREEN + "You must select either (1) or (2) for\
 'Yes' or 'No'")
        print(colorama.Fore.YELLOW + "1. Yes")
        print(colorama.Fore.YELLOW + "2. No")

        cinema = input("Please submit your answer now: ")

        if cinema in ['1', '2']:
            film_data.append(int(cinema))
            print(colorama.Fore.GREEN + "We have collected this data,\
 thank you and on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this\
 answer is invalid.")
            print(colorama.Fore.RED + "Please enter the number either\
 ('1') or ('2') depending on your choice..")
            time.sleep(2)
            clear()

    # Bonus Question 2
    while True:
        print(colorama.Fore.CYAN + "Bonus Question Two: What day do you\
 usually go to the cinema?")
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
            print("We have collected this data, thank you and\
 on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "The answer you have\
 submitted is invalid.")
            print(colorama.Fore.RED + "Please submit a number, between\
 '1' or '7' depending on your preference.")
            time.sleep(2)
            clear()

    # Question 5
    while True:
        print(colorama.Fore.YELLOW + "Question Five: From this selection what\
 is your favourite genre of film\n ")
        print(colorama.Fore.YELLOW + "1. Action")
        print(colorama.Fore.YELLOW + "2. Drama")
        print(colorama.Fore.YELLOW + "3. Crime/Thriller")
        print(colorama.Fore.YELLOW + "4. Romance")
        print(colorama.Fore.YELLOW + "5. Comedy")
        print(colorama.Fore.YELLOW + "6. Sci-Fi")
        print(colorama.Fore.YELLOW + "7. Other\n")
        print(colorama.Fore.GREEN + "In this question you must select an\
 answer between the numbers 1 and 7 depending on your preference.\n")
        genre = input("Please select an option now: ")

        if genre in ['1', '2', '3', '4', '5', '6', '7']:
            film_data.append(genre)
            print("We have collected this data, thank you and on to\
 the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "Sorry but this entry is invalid.")
            print(colorama.Fore.RED + "You must select a number from 1-7")
            time.sleep(2)
            clear()

    # Bonus Question 3
    if genre == '1':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite action movie?")
    elif genre == '2':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite drama movie?")
    elif genre == '3':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite crime movie?")
    elif genre == '4':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite romance movie?")
    elif genre == '5':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite comedy movie?")
    elif genre == '6':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 all-time favorite Sci-Fi movie?")
    elif genre == '7':
        print(colorama.Fore.CYAN + "Bonus Question Three: I see that you\
 have selected 'Other'\
 I'll simply ask what is your all-time favorite movie?\n")

    favorite = input("Please enter your answer: ")
    bonus_data.append(favorite)

    print(colorama.Fore.CYAN + f"Thank you for answering {user_name},\
 on to the final question!")
    time.sleep(2)
    clear()

    while True:
        print(colorama.Fore.YELLOW + "Question Six: When will you\
 watch your next movie?\n")
        print(colorama.Fore.YELLOW + "1. Today")
        print(colorama.Fore.YELLOW + "2. This Week")
        print(colorama.Fore.YELLOW + "3. This Month")
        print(colorama.Fore.YELLOW + "4. This Year")

        watch_movie = input("Please enter your answer now: ")
        if watch_movie in ['1', '2', '3', '4']:
            film_data.append(watch_movie)
            print(colorama.Fore.GREEN + f"Thank you for\
 answering {user_name}.")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "Sorry but this answer is invalid.")
            print(colorama.Fore.RED + "Please enter a value between [1-4]")
            time.sleep(2)
            clear()

    # Append data to Google Sheets
    try:
        film_survey_worksheet = SHEET.worksheet("film")
        film_survey_worksheet.append_row(film_data)
        bonus_survey_worksheet = SHEET.worksheet("bonus")
        bonus_survey_worksheet.append_row(bonus_data)
    except Exception as e:
        print(colorama.Fore.RED + "An error occurred while appending\
 the data to Google Sheets:")
        print(colorama.Fore.RED + str(e))

    print("Calling end_survey_film() now...")  # Debugging statement
    end_survey_film()  # Call the end_survey_film function here to\
    # conclude the survey


"""
This function was created as a personalised
way to end the film survey.
"""


def end_survey_film():

    global user_choice   # Creating a global variable to ensure\
    # that the right survey details are shown
    user_choice = '1'
    clear()
    print(f"Thank you for taking this film survey, {user_name}!")
    print("This survey and the data recorded will help us understand")
    print("the mindset of a film enthusiast in 2024.\n")
    print("I'm sure you're keen to know just how everybody\
 who has completed")
    print("this survey has gotten on, so please select the option to\
 'View Statistics'.\n")
    print("However, if you want to just exit the program then please\
 select 'Exit'.\n")
    print("1. View Statistics")
    print("2. Exit")

    while True:
        choice = input("Where would you like to go (1) or (2)? ")
        if choice == '1':
            view_statistics()
            break
        elif choice == '2':
            clear()
            print(colorama.Fore.GREEN + "Exiting the Survey")
            print("Thank you for your time!")
            time.sleep(2)
            print("Your data submitted in this survey will be stored.")
            print("May we meet again in another survey!")
            time.sleep(3)
            clear()
            exit()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, that is invalid.")
            print("Please enter the number (1) or (2).")


"""
This function book_survey was created for users who selected Option 2
"Bookreaders" in the entry question in this project.
It has questions tailor-made
so that bookreaders can honestly complete it.
"""


def book_survey():
    if user_name is None:
        print(colorama.Fore.RED + "Error: User name not set. Please start\
 the survey again.")
        return

    print(colorama.Fore.GREEN + "The book survey will now begin!")
    time.sleep(3)
    clear()

    print(colorama.Fore.GREEN + f"Once again, welcome {user_name},\
 we are thrilled that you have")
    print(colorama.Fore.GREEN + "taken the time to take this short survey!\n")
    time.sleep(4)
    print(colorama.Fore.GREEN + "As you have selected option 2 'Bookreader'\
 we have taken this into account")
    print(colorama.Fore.GREEN + "and have built a tailor-made survey just\
 for you to dive into.")
    print(colorama.Fore.GREEN + "It's now time to sit back, get a drink\
 or some popcorn, and answer a few questions!")
    time.sleep(5)
    clear()

    book_data = []
    bonus_book_data = []

    # Question 1
    while True:
        print(colorama.Fore.YELLOW + "Question One: From a scale of 1-10\
 please tell me how")
        print(colorama.Fore.YELLOW + "often you read books\n")
        print(colorama.Fore.GREEN + "You must answer this question with\
 numbers ranging from 1-10")
        print(colorama.Fore.GREEN + "(1 is extremely rarely,\
 10 is all the time).")
        try:
            often_read = int(input("Please enter a rating between 1-10: "))
            if 1 <= often_read <= 10:
                book_data.append(str(often_read))  # Convert to string for \
                # consistency
                print("We have collected this data, thank you and\
 on to the next question!")
                time.sleep(2)
                clear()
                break
            else:
                print(colorama.Fore.RED + "Invalid rating.")
                print(colorama.Fore.RED + "Please enter a number\
 between 1 and 10.")
                time.sleep(2)
                clear()
        except ValueError:
            print(colorama.Fore.RED + "Invalid input.")
            print(colorama.Fore.RED + "Please enter a number between\
 1 and 10.")
            time.sleep(2)
            clear()

    # Bonus Book Question 1
    while True:
        print(colorama.Fore.CYAN + "Bonus Question One: Have you ever\
 been to a book convention?\n")
        print(colorama.Fore.CYAN + "1. Yes")
        print(colorama.Fore.CYAN + "2. No\n")
        print(colorama.Fore.GREEN + "You must answer this question\
 with the numbers (1) or (2).")

        convention = input("Please enter your answer: ")
        if convention in ['1', '2']:
            bonus_book_data.append(convention)
            print("We have collected this data, thank you and on to\
 the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name},\
 this answer is invalid.")
            print("You must answer with the numbers (1) or (2).")
            time.sleep(2)
            clear()

    # Question 2
    while True:
        print(colorama.Fore.YELLOW + "Question Two: What type of books\
 do you read/view?\n")
        print(colorama.Fore.YELLOW + "1. Physical Books")
        print(colorama.Fore.YELLOW + "2. E-books")
        print(colorama.Fore.YELLOW + "3. Audiobooks")
        print(colorama.Fore.GREEN + "You must enter a value between\
 (1-3) based on your preference.")

        book_type = input("Please enter your answer now: ")
        if book_type in ['1', '2', '3']:
            book_data.append(book_type)
            print("We have collected this data, thank you and\
 on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this\
 answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between\
 the numbers (1-3)")
            time.sleep(2)
            clear()

    # Question 3
    while True:
        print(colorama.Fore.YELLOW + "Question Three: When you purchase\
 a book how important is the")
        print(colorama.Fore.YELLOW + "cover-art in the psychology of\
 making your purchase\n")
        print(colorama.Fore.YELLOW + "1. Very Important")
        print(colorama.Fore.YELLOW + "2. Somewhat Important")
        print(colorama.Fore.YELLOW + "3. Not Very Important")
        print(colorama.Fore.YELLOW + "4. Not at all Important\n")
        print(colorama.Fore.GREEN + "You must enter a value between (1-4)\
 based on your preference.")

        cover_art = input("Please enter your answer now: ")
        if cover_art in ['1', '2', '3', '4']:
            book_data.append(cover_art)
            print(colorama.Fore.GREEN + "We have collected this data,\
 thank you and on tothe next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this\
 answer is invalid")
            print(colorama.Fore.RED + "Your answer must be between\
 the numbers (1-4)")
            time.sleep(2)
            clear()

    # Bonus Question Two
    while True:
        print(colorama.Fore.CYAN + "Bonus Question Two: What type of\
 book-cover attracts your eye?\n")
        print(colorama.Fore.CYAN + "1. Colorful")
        print(colorama.Fore.CYAN + "2. Interesting Picture")
        print(colorama.Fore.CYAN + "3. Material")
        print(colorama.Fore.CYAN + "4. Comments on Cover")

        print(colorama.Fore.GREEN + "Please select an option through (1-4)\
 using the numbers (1-4)")
        attract = input("Please submit your answer: ")
        if attract in ['1', '2', '3', '4']:
            bonus_book_data.append(attract)
            print("We have collected this data, thank you and on to the\
 next question!")
            time.sleep(2)
            clear()

            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer\
 is invalid")
            print(colorama.Fore.RED + "Your answer must be between the\
 numbers (1-4)")
            time.sleep(2)
            clear()

    # Question 4
    while True:
        print(colorama.Fore.YELLOW + "Question Four: Roughly, how many hours\
 do you spend reading")
        print(colorama.Fore.YELLOW + "a book at once during one book-reading\
 session?\n")
        print(colorama.Fore.YELLOW + "1. Under an hour")
        print(colorama.Fore.YELLOW + "2. 1-2 hours")
        print(colorama.Fore.YELLOW + "3. 2-4 hours")
        print(colorama.Fore.YELLOW + "4. Over 4 hours")

        read_hours = input("Please submit your answer: ")
        if read_hours in ['1', '2', '3', '4']:
            book_data.append(read_hours)
            print(colorama.Fore.GREEN + "We have collected this\
 data, thank you and on to the next question!")
            time.sleep(2)
            clear()

            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, this answer\
 is invalid")
            print(colorama.Fore.RED + "Your answer must be between the\
 numbers (1-4)")
            time.sleep(2)
            clear()

    # Question 5
    while True:
        print(colorama.Fore.YELLOW + "Question Five: From this selection\
 what is your favourite genre of book/novel\n ")
        print(colorama.Fore.YELLOW + "1. Fantasy")
        print(colorama.Fore.YELLOW + "2. Dystopian")
        print(colorama.Fore.YELLOW + "3. Romance Novel")
        print(colorama.Fore.YELLOW + "4. Horror")
        print(colorama.Fore.YELLOW + "5. Biography")
        print(colorama.Fore.YELLOW + "6. Historical Fiction")
        print(colorama.Fore.YELLOW + "7. Science Fiction")
        print(colorama.Fore.YELLOW + "8. Action")
        print(colorama.Fore.YELLOW + "9. Childrens")
        print(colorama.Fore.YELLOW + "10. Mystery\n")

        book_genre = input("Please submit your answer: ")
        if book_genre in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            book_data.append(book_genre)
            print(colorama.Fore.GREEN + "We have collected this\
 data, thank you and on to the next question!")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "Sorry but this entry is invalid.")
            print(colorama.Fore.RED + "You must select a number from 1-10")
            time.sleep(2)
            clear()

    # Bonus Question 3
    if book_genre == '1':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite fantasy novel?")
    elif book_genre == '2':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite dystopian novel?")
    elif book_genre == '3':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite romance novel?")
    elif book_genre == '4':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite horror novel?")
    elif book_genre == '5':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite biography?")
    elif book_genre == '6':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite historical fiction novel?")
    elif book_genre == '7':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite science fiction novel?")
    elif book_genre == '8':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite action novel?")
    elif book_genre == '9':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favouirite childrens book?")
    elif book_genre == '10':
        print(colorama.Fore.CYAN + "Bonus Question Three: What is your\
 favourite mystery novel?")

    book_favorite = input("Please enter your answer: ")
    bonus_book_data.append(book_favorite)

    print(colorama.Fore.CYAN + f"Thank you for answering {user_name}, on\
 to the final question!")
    time.sleep(2)
    clear()

    # Question 6
    while True:
        print(colorama.Fore.YELLOW + "Question Six: When will you read\
 your next book?\n")
        print(colorama.Fore.YELLOW + "1. Today")
        print(colorama.Fore.YELLOW + "2. This Week")
        print(colorama.Fore.YELLOW + "3. This Month")
        print(colorama.Fore.YELLOW + "4. This Year")

        reading = input("Please enter your answer now: ")
        if reading in ['1', '2', '3', '4']:
            book_data.append(reading)
            print(colorama.Fore.GREEN + f"Thank you for\
 answering {user_name}.")
            time.sleep(2)
            clear()
            break
        else:
            print(colorama.Fore.RED + "Sorry but this answer is invalid.")
            print(colorama.Fore.RED + "Please enter a value between [1-4]")
            time.sleep(2)
            clear()

    # This allows for the data to append to Google Sheets
    try:
        book_survey_worksheet = SHEET.worksheet('book')
        book_survey_worksheet.append_row(book_data)
        bonus_book_survey_worksheet = SHEET.worksheet('bookbonus')
        bonus_book_survey_worksheet.append_row(bonus_book_data)
        print(colorama.Fore.GREEN + "Book survey data has been\
 successfully recorded.")
    except Exception as e:
        print(colorama.Fore.RED + "An error occurred while appending the\
 data to Google Sheets:")
        print(colorama.Fore.RED + str(e))

    end_survey_book()


"""
This function was created so it has a personalised
end route for those who picked book survey
"""


def end_survey_book():
    global user_choice
    user_choice = '2'
    clear()
    print(f"Thank you for taking this book survey, {user_name}!")
    print("This survey and the data recorded will help us understand")
    print("the mindset of a film enthusiast in 2024.\n")

    print("I'm sure you're keen to know just how everybody who has completed")
    print("this survey has gotten on, so please select the \
 option to 'View Statistics'.\n")
    print("However, if you want to just exit the program\
 then please select 'Exit'.\n")

    print("1. View Statistics")
    print("2. Exit")

    while True:
        choice = input("Where would you like to go (1) or (2)? ")
        if choice == '1':
            view_statistics()
            break
        elif choice == '2':
            clear()
            print(colorama.Fore.GREEN + "Exiting the Survey")
            print("Thank you for your time!")
            time.sleep(2)
            print("Your data submitted in this survey will be stored.")
            print("May we meet again in another survey!")
            time.sleep(3)
            clear()
            exit()
            break
        else:
            print(colorama.Fore.RED + f"Sorry {user_name}, that is invalid.")
            print("Please enter the number (1) or (2).")


def view_statistics():
    clear()
    print(colorama.Fore.GREEN + "Fetching survey statistics...")
    time.sleep(2)
    clear()

    # Initialize counts dictionaries
    film_counts = {
        'Super Enthusiasm': 0,
        'Moderate Enthusiasm': 0,
        'Mild Enthusiasm': 0,
        'Little Enthusiasm': 0,
        'Ratings': [],
        'Average Watching': [],
        'Cinema Visits': {
            'Yes': 0,
            'No': 0
            },
        'Genres': {
                'Action': 0,
                'Drama': 0,
                'Crime/Thriller': 0,
                'Romance': 0,
                'Comedy': 0,
                'Sci-Fi': 0,
                'Other': 0
                },
        'Next Movie Watch Time': {
                    'Today': 0,
                    'This Week': 0,
                    'This Month': 0,
                    'This Year': 0
                    }
                    }

    bonus_film_counts = {
        'Snack Purchases': {
            'Yes': 0,
            'No': 0
            },
        'Going Cinema': {
                'Monday': 0,
                'Tuesday': 0,
                'Wednesday': 0,
                'Thursday': 0,
                'Friday': 0,
                'Saturday': 0,
                'Sunday': 0
                }
                }

    book_counts = {
        'Reading Frequency': [],
        'Book Convention Attendance': {
            'Yes': 0,
            'No': 0
            },
        'Book Types': {
                'Physical Books': 0,
                'E-books': 0,
                'Audiobooks': 0
                },
        'Cover Art Importance': {
                    'Very Important': 0,
                    'Somewhat Important': 0,
                    'Not Very Important': 0,
                    'Not at all Important': 0
                    },
        'Cover Attraction': {
                        'Colorful': 0,
                        'Interesting Picture': 0,
                        'Material': 0,
                        'Comments on Cover': 0
                         },
        'Reading Duration': {
                            'Under an hour': 0,
                            '1-2 hours': 0,
                            '2-4 hours': 0,
                            'Over 4 hours': 0
                            },
                        'Genres': {
                                'Fantasy': 0,
                                'Dystopian': 0,
                                'Romance Novel': 0,
                                'Horror': 0,
                                'Biography': 0,
                                'Historical Fiction': 0,
                                'Science Fiction': 0,
                                'Action': 0,
                                'Children’s': 0,
                                'Mystery': 0
                                 },
                                'Next Book Read Time': {
                                    'Today': 0,
                                    'This Week': 0,
                                    'This Month': 0,
                                    'This Year': 0
                                    }
                                    }

    bonus_book_counts = {
        'Book Convention Attendance': {
            'Yes': 0,
            'No': 0
            },
        'Cover Attraction': {
                'Colorful': 0,
                'Interesting Picture': 0,
                'Material': 0,
                'Comments on Cover': 0
                }
                }

    film_worksheet = SHEET.worksheet("film")
    film_data = film_worksheet.get_all_records()

    bonus_worksheet = SHEET.worksheet("bonus")
    bonus_data = bonus_worksheet.get_all_records()

    book_worksheet = SHEET.worksheet("book")
    book_data = book_worksheet.get_all_records()

    bonus_book_worksheet = SHEET.worksheet("bookbonus")
    bonus_book_data = bonus_book_worksheet.get_all_records()

    for row in film_data:

        enthusiasm = int(row.get('Enthusiasm', 0))
        if enthusiasm == 1:
            film_counts['Super Enthusiasm'] += 1
        elif enthusiasm == 2:
            film_counts['Moderate Enthusiasm'] += 1
        elif enthusiasm == 3:
            film_counts['Mild Enthusiasm'] += 1
        elif enthusiasm == 4:
            film_counts['Little Enthusiasm'] += 1

        film_counts['Ratings'].append(int(row.get('Cinema Rating', 0)))

        film_counts['Average Watching'].append(int(row.get('How often\
 you watch Movies?', 0)))

        cinema_visit = row.get('Cinema Visit', '2')
        if cinema_visit == 1:
            film_counts['Cinema Visits']['Yes'] += 1
        else:
            film_counts['Cinema Visits']['No'] += 1

        genre = row.get('Genre', 0)
        if genre == 1:
            film_counts['Genres']['Action'] += 1
        elif genre == 2:
            film_counts['Genres']['Drama'] += 1
        elif genre == 3:
            film_counts['Genres']['Crime/Thriller'] += 1
        elif genre == 4:
            film_counts['Genres']['Romance'] += 1
        elif genre == 5:
            film_counts['Genres']['Comedy'] += 1
        elif genre == 6:
            film_counts['Genres']['Sci-Fi'] += 1
        elif genre == 7:
            film_counts['Genres']['Other'] += 1

        watch = (row.get('When will you watch your next movie?', 0))
        if watch == 1:
            film_counts['Next Movie Watch Time']['Today'] += 1
        elif watch == 2:
            film_counts['Next Movie Watch Time']['This Week'] += 1
        elif watch == 3:
            film_counts['Next Movie Watch Time']['This Month'] += 1
        elif watch == 4:
            film_counts['Next Movie Watch Time']['This Year'] += 1

        # Process bonus film data

    for row in bonus_data:

        snack_purchase = int(row.get('Snack Purchase', 2))
        if snack_purchase == 1:
            bonus_film_counts['Snack Purchases']['Yes'] += 1
        else:
            bonus_film_counts['Snack Purchases']['No'] += 1

        cinema_day = int(row.get('Cinema Day', 0))
        if cinema_day == 1:
            bonus_film_counts['Going Cinema']['Monday'] += 1
        elif cinema_day == 2:
            bonus_film_counts['Going Cinema']['Tuesday'] += 1
        elif cinema_day == 3:
            bonus_film_counts['Going Cinema']['Wednesday'] += 1
        elif cinema_day == 4:
            bonus_film_counts['Going Cinema']['Thursday'] += 1
        elif cinema_day == 5:
            bonus_film_counts['Going Cinema']['Friday'] += 1
        elif cinema_day == 6:
            bonus_film_counts['Going Cinema']['Saturday'] += 1
        elif cinema_day == 7:
            bonus_film_counts['Going Cinema']['Sunday'] += 1

        # Process book data

    for row in book_data:
        reading_freq = int(row.get('Reading Frequency', 0))
        book_counts['Reading Frequency'].append(reading_freq)

        book_type = row.get('Book Type', 'Physical Books')
        if book_type == 1:
            book_counts['Book Types']['Physical Books'] += 1
        elif book_type == 2:
            book_counts['Book Types']['E-books'] += 1
        elif book_type == 3:
            book_counts['Book Types']['Audiobooks'] += 1

        cover_art = int(row.get('Cover Art Importance', 'Not at all\
 Important'))
        if cover_art == 1:
            book_counts['Cover Art Importance']['Very Important'] += 1
        elif cover_art == 2:
            book_counts['Cover Art Importance']['Somewhat Important'] += 1
        elif cover_art == 3:
            book_counts['Cover Art Importance']['Not Very Important'] += 1
        elif cover_art == 4:
            book_counts['Cover Art Importance']['Not at all\
 Important'] += 1

        reading_duration = row.get('Reading Duration', 'Under an hour')
        if reading_duration == 1:
            book_counts['Reading Duration']['Under an hour'] += 1
        elif reading_duration == 2:
            book_counts['Reading Duration']['1-2 hours'] += 1
        elif reading_duration == 3:
            book_counts['Reading Duration']['2-4 hours'] += 1
        elif reading_duration == 4:
            book_counts['Reading Duration']['Over 4 hours'] += 1

        book_genre = (row.get('Book Genre',))
        if book_genre == 1:
            book_counts['Genres']['Fantasy'] += 1
        elif book_genre == 2:
            book_counts['Genres']['Dystopian'] += 1
        elif book_genre == 3:
            book_counts['Genres']['Romance Novel'] += 1
        elif book_genre == 4:
            book_counts['Genres']['Horror'] += 1
        elif book_genre == 5:
            book_counts['Genres']['Biography'] += 1
        elif book_genre == 6:
            book_counts['Genres']['Historical Fiction'] += 1
        elif book_genre == 7:
            book_counts['Genres']['Science Fiction'] += 1
        elif book_genre == 8:
            book_counts['Genres']['Action'] += 1
        elif book_genre == 9:
            book_counts['Genres']['Children’s'] += 1
        elif book_genre == 10:
            book_counts['Genres']['Mystery'] += 1

        read_book = row.get('When will you next read a book?', 0)
        if read_book == 1:
            book_counts['Next Book Read Time']['Today'] += 1
        elif read_book == 2:
            book_counts['Next Book Read Time']['This Week'] += 1
        elif read_book == 3:
            book_counts['Next Book Read Time']['This Month'] += 1
        elif read_book == 4:
            book_counts['Next Book Read Time']['This Year'] += 1

        # Process bonus book data
    for row in bonus_book_data:

        convention_attendance = row.get('Book Convention Attendance', '2')
        if convention_attendance == 1:
            bonus_book_counts['Book Convention Attendance']['Yes'] += 1
        else:
            bonus_book_counts['Book Convention Attendance']['No'] += 1

        cover_attr = row.get('Cover Attraction', 'Colorful')
        if cover_attr == 1:
            bonus_book_counts['Cover Attraction']['Colorful'] += 1
        elif cover_attr == 2:
            bonus_book_counts['Cover Attraction']['Interesting\
 Picture'] += 1
        elif cover_attr == 3:
            bonus_book_counts['Cover Attraction']['Material'] += 1
        elif cover_attr == 4:
            bonus_book_counts['Cover Attraction']['Comments on Cover'] += 1

    # Print out statistics
    print(colorama.Fore.GREEN + "\nFilm Survey Statistics:\n")
    print(colorama.Fore.YELLOW + f"Super Enthusiasm:\
 {film_counts['Super Enthusiasm']}")
    print(f"Moderate Enthusiasm: {film_counts['Moderate Enthusiasm']}")
    print(f"Mild Enthusiasm: {film_counts['Mild Enthusiasm']}")
    print(f"Little Enthusiasm: {film_counts['Little Enthusiasm']}\n")

    print(f"Average Cinema Rating in 2024: {sum(film_counts['Ratings'\
 ]) / len(film_counts['Ratings']) if film_counts['Ratings'] else 0}")
    print(f"Average Watching: {sum(film_counts['Average Watching'\
 ]) / len(film_counts['Average Watching']) if film_counts['Average\
 Watching'] else 0}\n")

    print(f"Cinema Visits - Yes: {film_counts['Cinema Visits']['Yes']}, \
 No: {film_counts['Cinema Visits']['No']}")

    print(f"Genres: {film_counts['Genres']}")
    print(f"When will you watch your next movie?\
 {film_counts['Next Movie Watch Time']}\n")

    print(colorama.Fore.GREEN + "\nBonus Film Survey Statistics:\n")
    print(colorama.Fore.YELLOW + f"Snack Purchases\
 - Yes: {bonus_film_counts['Snack Purchases'\
]['Yes']}, No: {bonus_film_counts['Snack Purchases']['No']}")

    print(f"What day do you go to Cinema: \
 {bonus_film_counts['Going Cinema']}")

    print(colorama.Fore.GREEN + "\nBook Survey Statistics:\n")
    print(colorama.Fore.YELLOW + f"Reading Frequency:\
 {book_counts['Reading Frequency']}")
    print(f"Book Types: {book_counts['Book Types']}\n")
    print(f"Cover Art Importance: {book_counts['Cover Art Importance']}")
    print(f"Reading Duration: {book_counts['Reading Duration']}")
    print(f"Genres: {book_counts['Genres']}\n")
    print(f"When will you read your next book?\
  {book_counts['Next Book Read Time']}")

    print(colorama.Fore.GREEN + "\nBonus Book Survey Statistics:\n")
    print(colorama.Fore.YELLOW + f"Book Convention Attendance - Yes: \
  {bonus_book_counts['Book Convention Attendance']['Yes']}, No:\
  {bonus_book_counts['Book Convention Attendance']['No']}")

    print(f"Cover Attraction: {bonus_book_counts['Cover Attraction']}")

    while True:
        user_input = input("\nPress '1' to exit: (scroll up\
 for film stats) ")
        if user_input == '1':
            end_all()
            clear()


def end_all():
    clear()
    print("Thank you for taking the survey!")
    print("See you around!")
    time.sleep(3)
    clear()
    exit()


# Entry point of the script
welcome_message()
get_user_name_age()  # Collect the user’s name and age first
starting_page()
