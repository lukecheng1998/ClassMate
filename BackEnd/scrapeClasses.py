import requests
import json


def scrapeCourses():

    # Getting all subject abbreviations

    subject_url = 'https://api.purdue.io/odata/Subjects'
    subject_response = requests.get(subject_url)

    subject_data = json.loads(subject_response.text)
    subject_data = subject_data["value"]

    subjects = []
    for i in range(0, len(subject_data)):
        abb = subject_data[i]['Abbreviation']
        subjects.append(abb)

    # Getting all course numbers and titles

    courses = []
    keep_courses = []

    for abb in subjects:
        url = 'https://api.purdue.io/odata/Courses?$filter=Subject/Abbreviation eq \''
        url += abb
        url += '\'&$orderby=Number asc'
        response = requests.get(url)

        data = json.loads(response.text)
        data = data["value"]

        for i in range(0, len(data)):
            course_number = data[i]['Number']
            course_title = data[i]['Title']
            title = abb + ' ' + course_number + ': ' + course_title
            if '\'' in title:
                continue
            if title.lower() in keep_courses:
                continue
            keep_courses.append(title.lower())
            title.replace('\'', '')
            if title not in courses:
                courses.append(title)

    return courses
