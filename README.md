# Mahida's Film/Book Survey!

This extensive code heavy project is a Python based project that is deployed within a terminal. The survey is designed to be taken by users who are either film or book enthusiasts. The extensive nature of the code in this project allows users to choose between either a film or a book survey and depending on their choices they will recieve a tailor-made survey that respects their option. The key in this project was to create a fluid working survey using Python that stores data and can give it back to the user if they so wish by viewing the statistics in the sheet that stores the data entries of the survey. This project could have been 300 lines, 400 lines maybe 500 lines of code... However, the goal was to create a level of complexity and make sure users have many options to choose from and a reasonable amount of questions to answer. 

This page contains a single webpage called :
- run.py / **This file contains the code that is used in this project.**
- This is the link to the [Film/Book Survey](https://film-book-survey-35fbcf323ce8.herokuapp.com/)

## Table of Contents
<details>

<summary>Click here for the Table of Contents</summary>

- [Wireframes](#wireframes)
- [Features](#features)
- [User Stories](#user-stories)
- [UX](#ux)
- [Tools & Technologies](#tools--technologies)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

</details>

## Wireframes
- This is the initial mockup flowchart that was created in preperation to this project. As you can see within the project the detail has been increased from this with more options present.
- One of the details that is present that is not in this flowchart that has made it into the final edition of the program is raising exceptions and errors everytime the user inputs a non-valid submission for a question.  

![screenshot](documentation/mockup/flowchart.png)


## Features
- The features within this project are not as vividly clear as other projects for example those that use CSS or HTML to style and really take in the users eye. However, the features that are present are interactive as a lanuage like Python should hope to process.

- The program itself is terminal based meaning it's responsive and fast.
- The program additionally, stores the results of user's questions in the survey through Google Sheets that is activated through an API.
- The survey itself is designed to be taken by lovers of film or books and it is inclusive to all ages where humans can process information and come up with valid answers to improve the reliability of the entries in the survey. 
- The age chosen was 7-110.

### Existing Features

| Feature | Screenshot | Description |
| :---: | :---: | :---: |
| **Starting Screen** | ![screenshot](documentation/features/starting-features.png) | The starting screen of the program is designed to be as typical as a program activation can be with the words "Program Activated" |
| **Name and Age Collection** | ![screenshot](documentation/features/name-features.png) ![screenshot](documentation/features/age-features.png) | The collection of the name and age of the users |
| **Name and Age Errors** | ![screenshot](documentation/features/name-errorprompt-features.png) ![screenshot](documentation/features/age-errorprompt-features.png) | The program activates an error prompt when the user's entry is invalid and explains why. |
| **Survey Selection** | ![screenshot](documentation/features/surveychoice-features.png) | The program allows the user to select the survey they would like to take part in |
| **Return Name** | ![screenshot](documentation/features/return-feature.png) | The name that the user enters within the project is returned to them along with their option so that they understand what survey they are taking. It's good UX. |
| **Question 1** | ![screenshot](documentation/features/question1film-features.png) | The first question in the survey gives the user a choice of 4 options that are all given a value between (1-4) which will reflect on the Google sheet. |
| **Question 2** | ![screenshot](documentation/features/question2-features.png) | The second question in the film survey showcases that the questions differ in their entries. This question asks for a number between 1-10. |
| **Bonus Question** | ![screenshot](documentation/features/bonus-features.png) | The survey asks bonus questions to the user that are different in color to the normal questions that the user faces. These questions themselves are stored in a different sheet altogether. |
| **Question 5** | ![screenshot](documentation/features/Question5-features.png) | This table has shifted from Q2 straight to Q5 because the features in Q3 and Q4 are similar. The difference in Q5 is that the selection of the number that you pick directly gives you a question based on your choice right after this. |
| **Question 5 Follow Up Bonus** | ![screenshot](documentation/features/BonusQ3-features.png) | The follow-up question to Question 5 gives you a personalized question based on your choice in Q5. If the user picks option 7 in Q5 then they will receive this in 'Bonus Question Three'. |
| **Final Menu** | ![screenshot](documentation/features/finalmenu-features.png) ![screenshot](documentation/features/bookfinal-features.png) | This final menu is brought up when the user completes the questions in the survey. The menu is personalized showing the user's name and what survey they have taken. The book survey additionally shows that they have taken the book survey. |
| **Final Options** | ![screenshot](documentation/features/finaloptions-features.png) | The final menu contains two different options: 1. View Statistics, 2. Exit. These options allow the user to either check the results of the survey by all users that have completed it. The second option closes the survey completely. |
| **Exit Message** | ![screenshot](documentation/features/exit-features.png) | There is an exit message that shows once the user selects the exit option. |
| **Stats** | ![screenshot](documentation/features/film-stats.png) ![screenshot](documentation/features/book-stats.png) | The statistics function when activated by the user with their choice showcases the survey results from every single user that has taken the survey. This displays both the film survey and the book survey results that have been processed and delivered to the program with Google Sheets. |

- It is important to understand that these are the main features in the project. The book survey operates exactly the same so I've refrained from adding more descriptions in this table to avoid repititon.

### Future Features
- When I return to this project I would like to add more features that personalize the users experience even more with additional prompts and questions designed to take into account the users previous answers so the survey can feel complex and progressive for the users taking it.
- Additonally, I would love to create a detailed homescreen that provides a spoiler in some ways to what both sides of the survey will entail.

## User Stories
1. As a new user I want to be able to take a fast and easy survey.
2. As a new user, I want to be able to have a preference in either a book or film survey.
3. As a new user, I want to be able to see that the options I choose are reflected back to me in the survey.
4. As a new user, I want the program to understand when I have made an invalid answer.
5. As a new user, once I complete the survey I want to have a clear method of exiting and knowing that the survey is done.
6. As a new user, once I complete the survey I want to have a look at the results of the survey that has been gathered by everybody who has taken it.

## UX
- The project takes use of a command line terminal so there isn't much that is designed to draw the user in with colors, images and videos etc. There isn't a whole lot of options at the disposal of this project. However, as showcased in the features above there are still many different aspects of this project that is designed to make sure the user has a good experience. 

- One of these were the collection of the name and age of the user, this ensures that the user feels involved and valued with their names being returned back to them by the program. It shows initiative and care. 
- Another aspect that is critical to the experience of the user is the relay of data within the statistics so they understand that the survey is not for nothing. There is actual evidence that data is being stored, updated and used. 

- The data model in this project was simply Google Sheets which is a very easy and helpful tool for storing data and retrieving data if anybody reading this README file would like to replicate the project. 

![names](documentation/images/name-sheet.png)
![film](documentation/images/film-sheet.png)
![bonus](documentation/images/bonus-sheet.png)
![book](documentation/images/book-sheet.png)
![bookbonus](documentation/images/bookbonus-sheet.png)

[Spreadsheet link](https://docs.google.com/spreadsheets/d/1CItEB8EXjVia5hxisD0COsFiaz57bzeuxEqTMk5rooI/edit?usp=sharing)


### Color Scheme 
- The color scheme that is used in this project differs as the color is used only in text alone.
- The colors used are imported from colorama through the terminal. This allowed me to use colors that are provided by this program and they are as stated:
- `Yellow` this color was used mainly for the answers and the inputs.
- `Cyan`  this color was used mainly for the bonus questions to differentiate between them and the normal questions.
- `Green`  this color was used mainly for the text that isn't questions. This is for the text that tells the user what to do or gives information to the user.
- `Red`  this color was used to indicate to the user that something is wrong via an invalid answer/input and what they can do to solve it.


## Tools & Technologies 
- This is the tools and technologies used in this project. 
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) this language was used as the forefront of the project with all the code in the run.py file being Python.
- [HTML](https://en.wikipedia.org/wiki/HTML) this was used simply in the views folder to create a website terminal.
- [Git](https://git-scm.com/) used to control the site via "git add, git commit -m, git push" and etc.
- [GitHub](https://github.com/) was used to store my code and acess my project repository. 
- [VScode](https://code.visualstudio.com/) used as an IDE through GitPod.
- [Gitpod](https://www.gitpod.io/) used as the IDE to work and code the site.
- [Google Sheets](https://fonts.google.com/) was used to store survey data from the program and return survey data back in the form of stats.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) was used to deploy the project.


## Testing
 
 Please refer to the [TESTING.md](TESTING.md) file to see the testing of the website.

 ## Deployment
- This site was deployed via Heroku and not GitHub Pages. Therefore, steps to deploy on GitHub pages will not be present in this README.md file. However, steps to local deployment, forking, cloning and the main deployment to Heroku will be detailed in full so you can replicate this project or have a better understanding of deployment. 

### Local Deployment 



### Cloning 




## Credits


##  Acknowledgements
