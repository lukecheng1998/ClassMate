import pyrebase
from getpass import getpass
import json


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

email = input("Please Enter Your Email Address: \n")
password = getpass("Please Enter a Password: \n")

#user = auth.create_user_with_email_and_password(email, password)

login = auth.sign_in_with_email_and_password(email, password)
print("Success")


