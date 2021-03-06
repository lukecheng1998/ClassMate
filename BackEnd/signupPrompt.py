import pyrebase
from getpass import getpass
import sys
import json
import mysql.connector
class signupPrompt():
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


  email = sys.argv[1] #we should replace the input with a variable passed in from the other py files
  password = sys.argv[2] #samething with password
  confirmPassword = sys.argv[3] #same with this one
  name = sys.argv[4]
  instagram = sys.argv[5]
  linkedin = sys.argv[6]
  if(confirmPassword != password):
      print("error passwords don't match") #we should try to find a way to send this back to the front end via a json or python equivilant
      sys.exit(1)
  #Uncommit the next few lines once the sql server is turned on

  #cnx = mysql.connector.connect(user='root', password='cs348',
  #                              host='35.202.58.216',
  #                              database='classmate')
  #cursor = cnx.cursor()
  #addUser = "INSERT INTO Users (puEmail, hashedPass, name, instagram, linkedin) VALUES(" + "'" + email + "'" + ", '" + password + "'" + ", '" + name + "'" + ", '" + instagram + "', '" + linkedin + "')"
  #cursor.execute(addUser)
  #cnx.commit()
  user = auth.create_user_with_email_and_password(email, password)
  db = firebase.database()
  newUserData = {
    "email":email,
    "fullName":name,
    "userId":user['localId']
  }
  db.child("users").child(email).set(newUserData)
  index = open("../templates/home.html").read()
  print("Success")
