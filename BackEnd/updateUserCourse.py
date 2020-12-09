import mysql.connector

cnx = mysql.connector.connect(user='root', password='cs348',
                              host='35.202.58.216',
                              database='classmate')

cursor = cnx.cursor()

# Get user data from front-end

user_email = ()
user_course = ()

# Delete data from the UserCourses table

delete_course = "DELETE FROM UserCourses WHERE user_email = " + str(user_email) + " AND user_course = " + str(user_course)

cursor.execute(delete_course)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()