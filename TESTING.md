Return to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Validation](#validation)
  - [Python](#python)
 
- [Lighthouse](#lighthouse)

- [User Story Testing](#user-story-testing)

- [Input Testing](#input-testing)

- [Manual Testing](#manual-testing)

- [Bugs](#bugs)

</details>

## Validation 
- This will show that the Python code is completely validated and correctly placed.

### Python

| Page | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| run.py | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](documentation/testing/pythonlinter-success.png) | Passed all checks |

## Lighthouse
Although Lighthouse isn't really a huge testing for this project, I've decided to include it to make sure I've taken every reasonable step in testing.

| Page   | Mobile                                                                                  | Desktop                                                                                   | Notes                                                                                                                                                                         |
| :----: | :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| run.py | ![screenshot](documentation/testing/mobile-lighthouse.png) | ![screenshot](documentation/testing/desktop-lighthouse.png) | The site that the program is running on is running very well if not perfectly. The only hiccups that can be spotted with the 95 "Accessibility" score are completely out of my control due to the run program button and contrast issues. |

## User Story Testing 

| User Story | Screenshot |
| :---: | :---: |
| As a new user I want to be able to take a fast and easy survey. | ![screenshot](documentation/testing/uxtest-1.png) |
| As a new user, I want to be able to have a preference in either a book or film survey. | ![screenshot](documentation/features/surveychoice-features.png) |
| As a new user, I want to be able to see that the options I choose are reflected back to me in the survey. | ![screenshot](documentation/features/return-feature.png) |
| As a new user, I want the program to understand when I have made an invalid answer.| ![screenshot](documentation/testing/uxinvalid-testing.png) |
| As a new user, once I complete the survey I want to have a clear method of exiting and knowing that the survey is done.| ![screenshot](documentation/features/finaloptions-features.png) ![screenshot](documentation/features/finalmenu-features.png) |
| As a new user, once I complete the survey I want to have a look at the results of the survey that has been gathered by everybody who has taken it.| ![screenshot](documentation/features/film-stats.png) |

## Input Testing

- For the film and book sections of the survey all of the inputs work as expected and they will provide error messages incase there is a wrong submission that is placed in the input. I will go through each question and showcase this in a table with both book and film inputs being tested.

| Question | Film | Book | Notes |
| :---: | :---: | :---: | :---: |
| Question 1 | ![screenshot](documentation/testing/uxinvalid-testing.png) | ![screenshot](documentation/testing/bookq1invalid.png) | If there is an incorrect input in the input field an error message pops up defending the program. |
| Bonus Question 1 | ![screenshot](documentation/testing/filmbonusq1-invalid.png) | ![screenshot](documentation/testing/bookbonus1-error.png) | If there is an incorrect input it shows the error message defending the program. |
| Question 2 | ![screenshot](documentation/testing/filmq2-invalid.png) | ![screenshot](documentation/testing/bookq2-invalid.png) | If there is a wrong input then the error message pops up. |
| Question 3 | ![screenshot](documentation/testing/filmq3-invalid.png) | ![screenshot](documentation/testing/bookq3-invalid.png) | If there is a wrong input then the error message pops up. |
| Bonus Question 2 | ![screenshot](documentation/testing/filmbonusq2-invalid.png) | ![screenshot](documentation/testing/bookbonusq2-invalid.png) | If there is a wrong input then the error message pops up. |
| Question 4 | ![screenshot](documentation/testing/filmq4-invalid.png) | ![screenshot](documentation/testing/bookq4-invalid.png) | If there is a wrong input then the error message pops up. |
| Question 5 | ![screenshot](documentation/testing/filmq5-invalid.png) | ![screenshot](documentation/testing/bookq5-invalid.png) | If there is a wrong input then the error message pops up. |
| Bonus Question 3 | ![screenshot](documentation/testing/filmbonusq3.png) | ![screenshot](documentation/testing/bookbonusq3.png) | There aren't any errors in this because this data although collected is not displayed and is a free entry for the user to tell what their favourite film is. |
| Question 6 | ![screenshot](documentation/testing/filmq6-invalid.png) | ![screenshot](documentation/testing/bookq6-invalid.png) | If there is a wrong input then the error message pops up. |

- The reason that bonus data 3 is not shown back to the user is simply for the user experience. the amount of entries that are placed will flood the statistics making it hard to read and adding too much visual clutter where it really is not needed. The crucial data the data that is analytical is processed and is delievered to the user that's the data that matter, that's the data that counts. 

- There are additional errors catching statements.
![screenshot](documentation/features/age-errorprompt-features.png)
![screenshot](documentation/features/name-errorprompt-features.png)
![screenshot](documentation/testing/finalmenu-test.png)




