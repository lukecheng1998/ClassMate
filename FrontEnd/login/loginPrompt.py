import pyrebase
from getpass import getpass
import json
import requests
import sys
from firebase_admin import auth

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
auth1 = firebase.auth()
db = firebase.database()

email = sys.argv[1]
password = sys.argv[2]

#user = auth.create_user_with_email_and_password(email, password)

login = auth1.sign_in_with_email_and_password(email, password)
if(login):
  print("Success")
  #print(login)
  print(login['idToken'])
else:
  print("Failed")




