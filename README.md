# FARMART BACKEND 

## DATE : 18TH NOV 2024

## FarmArt API
FarmArt is an API designed to support a farm management system where users can view and interact with farmers, animals, and orders. Users can add animals to their cart, place orders, and checkout through the system. The application supports JWT authentication to secure the endpoints.

## Features
- **JWT Authentication**: Secure access to endpoints with JWT tokens.
- **Farmers**: Add, update, delete, and view farmers' information.
- **Animals**: Add, update, delete, and view animals associated with farmers.
- **Orders**: Create, update, delete, and view orders placed by users for animals.
- **Cart**: Users can add animals to their cart before placing an order.
- **User Management**: Register, login, update, and delete user accounts.
  


## LEARNING GOALS
-Implement an app using python language and flask framework.

### Instructions
##### Final Project
This is the time to dive into React libraries you've gotten interested in, or play with APIs that would have taken too long to figure out during a shorter project week. This is the time to make the app that you've always wanted but never had, write up a bunch of custom CSS, and really put your skills on display.

Because we're asking you to show off a specific set of skills, we have some requirements. It should be obvious that one of the requirements is that you need to use the things that you learned during this course. This isn't the time to build a game with Unity or explore the MEAN stack or try and whip up a React Native app. You've done a ton of learning already — it's time to apply all of that knowledge.

### Project Requirements
You must meet the following Phase 5 Project Minimum Requirements:

- Implement Flask and SQLAlchemy in an application backend.
- Include a many to many relationship.
- Implement a minimum of 4 models.
- Implement a minimum of 5 client side routes using React router.
- Include full CRUD on at least 1 model, following REST conventions.
- Implement validations and error handling.
- Implement something new not taught in the curriculum. (Check in with your instructor to ensure the scope of your idea is appropriate.)
- Implement useContext or Redux.

** Please discuss with your instructor if you have any issues aligning these requirements with your project.

### Helpful Tools
#### Organization
**Kanban/Scrum Board:** Because this will be the most complex project you've made during this course, you'll need something to keep you organized. We recommend Trello or a Github Project Board. Use this to track what you're doing and what you need to work on. It's also a great idea to keep track of bugs that you're not going to immediately fix.

**Pomodoro Timer**: If you don't take breaks, you'll end up hurting your eyes, getting RSI (repetitive strain injury) or burning yourself out. The Pomodoro Timer method lets you put in solid chunks of work while also giving you regular breaks. We like Marinara Timer, since it's nicely customizable.

### Technology Stack
- Flask: A lightweight web application framework for Python.
- Flask-SQLAlchemy: An ORM that integrates SQLAlchemy with Flask.
- Flask-Migrate: For handling SQLAlchemy database migrations.
- Flask-JWT-Extended: JWT Authentication for securing API routes.
- SQLite: Relational database management system for storing data.
- Flask-RESTful: Extends Flask to build REST APIs easily.


### DATABASE
The database is structured using SQLAlchemy ORM and consists of the following tables:

- Users: Contains user details like id, name, email.
- Farmers: Contains farmer details like id, name, farm_name, and location.
- Animals: Contains animal details like id, type, breed, age, price, and the farmer_id as a foreign key.
- Orders: Contains order details like id, user_id, animal_id, total_price, and status.
- Cart: Contains items in the cart with user_id and animal_id.
- Tokens: Contains JWT token information, used to handle token invalidation.

### INSTALLATION
- To use this follow these steps:

### Alternative One
1.Open your terminal/cli on your computer. 

2.Clone the repository by running the following command:

    git clone https://github.com/ohnoitsmoraa/Farmart-backend.git

3.Change directory to the repo folder

    cd Farmart-backend
4.Open it in your Code Editor of choice. If you use VS Code, run the command:

    code .

### Alternative Two
1.On the top right corner of this page there is a button labelled Fork.

2.Click on that button to create a copy of the repository to your own account.

3.Follow the process described in Alternative One above.

4.Remember to replace your username when cloning.

    git clone https://github.com/ohnoitsmoraa/Farmart-backend.git

### Getting the files
Fork the repo, Create a new branch in your terminal & Install the prerequisite. Make appropriate changes in files. Run the server to see the changes Add the changes and commit them Push to the branch Create a pull request

Open the folder location on the terminal and use the following command to run the app:

### VERCEL LINK(LIVE LINK)
[live link to my webiste](https://r)

### HOW TO RUN ALL CODES
clone the repository run using live server

### Environment Variables
- SQLALCHEMY_DATABASE_URI: The URI for connecting to the PostgreSQL database.
- JWT_SECRET_KEY: A secret key for signing JWT tokens.
Endpoints

### DEPENDENCIES
practice Python and flask

### TECHNOLOGIES USED
Python,Flask

### TESTING
To run the tests, you'll need to have pytest installed. You can run the tests with the following command:

    pytest


### License
MIT  License