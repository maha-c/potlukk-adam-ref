# Potlukk
The application you are building is called Potlukk. It is an application for hosting potluck events and inviting other users. You will be given an early working prototype of the backend API. The API contains REST and GraphQL routes. Certain features like security have not been implemented on the server will be added by another team at a later date. You have been tasked with building the frontend for an API that is under development. The front end is not expected to be client ready but should be a workable demo for an upcoming stakeholder meeting. You will be provided.
- User Stories
- Application Diagrams
- Technical Requirements

## Due Dates
- ***2/7***
  - Signup page and user stories complete
- ***2/9***
  - Signin with redirect to home page. No functionality of home page expected
- ***2/14**
  - Host Page functionality complete
- ***2/20**
  - Due/ Presentations!!!
- During the week of 2/14 Rory and I will be checking your repos and github projects to make sure you are on track
### Project Expectations
- All MVP user stories must be complete
- Each page has been developed using proper BDD principles
  - Tests should be independent and use mocking when appropriate
    - Use nock and react testing library
- All code is in github
- Project is tracked and managed with github projects
- Github actions are used to
  - Test your code
  - Host your code on github pages
- **Failure to meet these requirements is grounds for an immediate drop**

### Key Terms
- **Lukker**
    - A user of the application
- **Potlukk**
  - A potluck
- **Host**
  - The Lukker who owns a particular Potlukk

## Set Up
1. install [python](https://www.python.org/downloads/) 
   1. Choose the default options and to install pip
2. clone this repository
3. in the directory with the main.py run `pip install -r requirements.txt`
4. run `pip install "uvicorn[standard]"`
5. in the directory with the main.py run the application with `uvicorn main:app` or `py -m uvicorn main:app --reload`
   1. *all data is persisted in memory*
   2. *restarting/stopping the application will erase data*
6. The applicaiton will run on port `http://localhost:8000`
   1. ***You can access interactable documentation of endpoints at `http://localhost:8000/docs`***


| As a    | I Want To | So That                                                                |    Priority |
|---------|-----------|------------------------------------------------------------------------|-------------|
| Lukker  | Sign In   | I can view my customized home page                                     | MVP |
| Lukker  | Register for an account            | Use the potlukk plaftform                     | MVP    |                  |          
| Lukker  | Create Potlukks | Host awesome events                                              | MVP |
| Lukker  | Add my allergies | I see clear warnings of Dishes I am allergic too                | MVP    |      
| Lukker  | Update my username and password | I can change my login information if wanted      | Stretch    |
| Lukker  | Search for potlukks by tags | Find public potlukks I might be interested in        | Stretch    |
| Lukker  | Say I am bringing a dish to the potlukk | Other guests do not bring the same thing | MVP     |
| Lukker  | Edit or remove the dishes I am brining | Guests avoid duplicates                   | MVP     |
| Host    | Create dishes for people to bring if possible| I can give suggestions to guests    | Stretch     |
| Host    | Edit the details of my Potlukk | I can keep everything up to date                  | MVP    |
| Host    | Create tags for my Potlukk | People can find my public potlukks                    | Stretch    |
| Host    | Edit the time or cancel my Potlukk | Attendees do not show up incorrectly           | MVP   |


## Fetatures by page
**Please refer to the draw.io file for a view of the pages**
- Some stretch features *do not* have diagrams
- You do not have to adhere strictly the diagram or structure of web pages
  - All functionality depecicted on a web page **Must be present**
  - The web pages should still be well spaced using flexblox and grid
    - Styling is not critical
    - Usage of a component library is *optional*
### Sign in
- User Features
  - A person can sign into their account
    - On success they are sent their home page
    - On failure they are given a pop up to try again
- Technical features
  - Axios or fetch to make the http request
  - Store user info in local storage

### Register
- User Features
  - A person can create an account
    - Form Validation
      - Password must have at least 10 characters and 1 special character or number
      - Password confirmation must match
    - Upon clicking register
      - Success
        - A popup must tell them they were successful and route them to their home page
      - Failure
        - They are given an alert saying what went wrong
- Technial Features
  - Store user info in local storage on success
  - Use axios or fetch for the http request
  - use the useReducer hook for form validation
  

### Home
- User Features
  - Three main lists are available for view
    - Hosted Potlukks
      - Shows potlukks the lukker is hosting
      - Clicking on one forwards the user to a potlukk details page for the potlukk
    - Invited Potlukks
      - Shows potlukks the lukker was invited too
      - Clicking on one forwards the user to a potlukk details page for the potlukk
    - Notifications
      - Shows all notifications that are related to the person
        - Events created by them 
        - Events that affect a potlukk they host or attend
- Technial Details
  - Use Redux-Thunks for making invite requests then showing the users you have invited
  - Navbar uses react router
  - clicking logout clears local storage and redirects to signin

### Host 
- User Features
  - Create a potlukk with time,date,location and description
  - Can search for lukkers by username 
    - Be able to invite people to a potlukk
  - Remove people who have been invited 
    - Once the host presses creates the invitation is final
  - User is given a confirmation prompt after pressing create
- Technical features
  - use React query for fetching and caching the information
  - Navbar uses react router
### Potlukk Details (Host)
- User features
  - Update my potlukk
  - Bring a dish of my own
  - Create a dish and leave it to be broughtBy someone else
    - The API assumes a dish requested to be broughtBy:0 
  - Edit or delete a dish I brought or requested
  - Invite more people
  - Cancel the potlukk
    - A confirmation prompt should double check the user's action
- Technical features
  - State management should be handled with redux
  - Saga should be used as a middle ware for asynchronous updates
 - Navbar uses react router
### Potlukk Details (Guest)
- User Features
  - Create a dish to bring
  - Edit or delete a dish I brought
  - Change my invitation status
- Technical features
  - State management should be handled with redux
  - Saga should be used as a middle ware for asynchronous updates
 - Navbar uses react router
### Tips
- ***START EARLY***
  - You will run into bugs and issues. The sooner you do the faster you can seek help and get them solved
- ***SEEK HELP***
  - If you get stuck on something for more than an hour reach out to another associate or the trainer
- ***TEST***
  - Testing is an investment in your time.
    - It is also a requirement
  - By testing as you develop you will save a tremendous amount of time 
    - You will not got a blank page with a vague error and no idea where it is coming from
- ***ONE STEP AT A TIME***
  - Tackle a page component by component
  - Tacke the application one page at a time
  - Components are resusable and moduler by design
- ***START EARLY***
  - I wanted to say this again!