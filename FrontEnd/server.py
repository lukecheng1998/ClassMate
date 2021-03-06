import pyrebase
from getpass import getpass
import json
import requests
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyDrDF0VPve6Nim45CEw8i4Lyo1L_cQ6Q3s",
    "authDomain": "classmate-293217.firebaseapp.com",
    "databaseURL": "https://classmate-293217.firebaseio.com",
    "projectId": "classmate-293217",
    "storageBucket": "classmate-293217.appspot.com",
    "messagingSenderId": "225751399217",
    "appId": "1:225751399217:web:9a54431dcf0f183a12ce10",
    "measurementId": "G-VQ21G1H5R1"
  }


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


@app.route('/signup/', methods=["POST"])
def signupPrompt():
    print('In sign up prompt')
    email = input("Please Enter Your Email Address: \n") #we should replace the input with a variable passed in from the other py files
    password = getpass("Please Enter a Password: \n") #samething with password
    confirmPassword = getpass("Please Confirm your password: \n") #same with this one
    name = input("Please write your name: \n")
    if(confirmPassword != password):
        print("error passwords don't match") #we should try to find a way to send this back to the front end via a json or python equivilant
        sys.exit(1)
    cnx = mysql.connector.connect(user='root', password='cs348',
                                  host='35.202.58.216',
                                  database='classmate')
    cursor = cnx.cursor()
    addUser = "INSERT INTO Users (puEmail, hashedPass, name, instagram, linkedin) VALUES(" + "'" + email + "'" + ", '" + password + "'" + ", '" + name + "'" + ", '', '')"
    cursor.execute(addUser)
    user = auth.create_user_with_email_and_password(email, password)
    print("Success")
@app.route('/login', methods=["POST"])
def loginPrompt(request):
    email = request.post['username']
    password = request.post['password']

    #user = auth.create_user_with_email_and_password(email, password)

    login = auth.sign_in_with_email_and_password(email, password)
    return render(request, "search.html", {'email': email})
    print("Success")
@app.route('/search')
def searchRoute:
    email = request.post['username']
    password = request.post['password']

    #user = auth.create_user_with_email_and_password(email, password)

    login = auth.sign_in_with_email_and_password(email, password)
    return render("search.html")