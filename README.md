Our Website is made for detecting any malicious behaviour in a PE file. If the uploaded PE file is malicious then it generates a warning message along with the log as a report for the same else if the file is safe it generates the alert and the log

Prerequisites:-

1. Make sure you have installed python(used version 3.12.2) in your system.

2. Install Django (used version 5.0.2) in your system. pip install django

3. In your vs code termonal install joblib using pip install joblib

4. Install sklearn. pip install scikit-learn

5. Install the PEFILE library pip install pefile

6. Install numpy library. pip install numpy

Steps to Access this project:-

1. For the project to run make sure you are currently in the 'bytedefender' folder. If you are in mywebsite folder move to bytedefender project by:- cd bytefender

2. Run your project using :- python manage.py runserver

3. After this you will recieve a url, click it to view our website.

Description of our website:-

1. HOME PAGE:- This is the landing page of our website. You can navigate to various pages of our websites using this.

2. SCAN PAGE:- To view this page the user will have to signup/login at first. In this page at first the user will upload the file which has to be scanned then the predictions will be made at the backend and the user will be diverted to the log page where the prediction along with the report will be displayed to the user.

3. HELP PAGE:- This is the page which contains the usage guidlines for our website and also some FAQs.

4. ABOUT PAGE:- This is the page which contains details of our website.

5. CONTACT PAGE:- User can send any of there queries to us using the contactus form provided here.

6. LOGIN PAGE:- If the user is already registered to our website he/she can directly login from here and get diverted to the scan page, if not then they will have to SIGNUP at first and then an Email will be sent to them and then it will get diverted to the scan page.
