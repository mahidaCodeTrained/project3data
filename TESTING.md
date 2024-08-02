Return to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Validation](#validation)
  - [Python](#python)
 
- [Lighthouse](#lighthouse)

- [User Story Testing](#user-story-testing)

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


