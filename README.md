# SuperU Assignment

# Steps to setup the project:

1. Clone the project
2. Install the required python libraries to run the project
   a. Create and select virtual environment ***python3 -m venv env / source env/bin/activate***.
   b. Install the library ***pip3 install requirements.txt***
3. Run the project using command - ***python3 manage.py runserver***
4. To execute the unit test cases -  ***python3 manage.py test***


# API Details
***Add Basic Authorization Header for Authentication - ***
<img width="993" alt="image" src="https://github.com/rijildaniel/superu_assignment/assets/40638987/4ff3fd09-36d6-49be-87b6-a2e71be7d56e">

***Username*** - admin@test.com
***Password*** - Test@1234

1. GET - (***http://127.0.0.1:8000/users/***) - To fetch list of users
2. POST  - (***http://127.0.0.1:8000/users/***) - To create new user profile
   Request Body - 
   <img width="653" alt="image" src="https://github.com/rijildaniel/superu_assignment/assets/40638987/3d61c8ef-a360-4600-bc6e-dc36f9ff369b">

4. PUT  - (***http://127.0.0.1:8000/users/***) - To create new user profile
   Request Body - 
   <img width="653" alt="image" src="https://github.com/rijildaniel/superu_assignment/assets/40638987/3d61c8ef-a360-4600-bc6e-dc36f9ff369b">
