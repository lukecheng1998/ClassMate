import mysql.connector

cnx = mysql.connector.connect(user='root', password='cs348',
                              host='35.202.58.216',
                              database='classmate')

cursor = cnx.cursor()

# Get user data from front-end

user_email = ()

# Get a users' courses

get_courses = "SELECT title FROM UserCourses WHERE puEmail = " + str(user_email)

cursor.execute(get_courses)

for course in cursor:
	print(course)

cursor.close()
cnx.close()