import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:' + 'cs348' + '@35.202.58.216:3306/classmate',
    echo=True)

# Get user data from front-end

user_email = ()
 
# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# Get a users' info

def getUserInfo():
    info = session.query(Users).filter(Users.puEmail = user_email)
    return info

# Get a users' friends

def getUserFriends():
    friends = session.query(UserFriends).join(Users).filter(UserFriends.puEmail1 = user_email OR UserFriends.puEmail2 = user_email)
    return friends
