import mysql.connector

import BackEnd.scrapeClasses
# pwd.py contains MyPassword = "1234"
# Username and password are stored in the python file for simplicity
# Do not store user credentials in your code,
# look for best security practices in your OS, database, and development environment

cnx = mysql.connector.connect(user='root', password='cs348',
                              host='35.202.58.216',
                              database='classmate')

cursor = cnx.cursor()

add_course = "INSERT INTO Courses (title) VALUES (%s)"

# Insert new course
courses = BackEnd.scrapeClasses.scrapeCourses()
for i in range(0, len(courses)):
    course_data = '\'' + courses[i] + '\''
    query = add_course % course_data
    cursor.execute(query)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()