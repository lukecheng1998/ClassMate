import mysql.connector

cnx = mysql.connector.connect(user='root', password='cs348',
                              host='35.202.58.216',
                              database='classmate')

cursor = cnx.cursor()

# Get user data from front-end

user_email = ()
user_course = ()

# Add data to the UserCourses table

add_course = "INSERT INTO UserCourses (puEmail, title) VALUES (%s, %s)"
course_data = (str(user_email), str(user_course))

cursor.execute(add_course, course_data)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()