from csv import DictReader

courses = []

with open('courses.csv', 'r', encoding= 'UTF-8') as file:
    reader = DictReader(file, fieldnames=['language', 'category'])
    try:
        for row in reader:
            courses.append({'language':row['language'], 'category':row['category']})
    except (KeyError):
        print('Deu bosta')

for course in sorted(courses, key= lambda course: course['language']):
    print(f'{course["language"]} - {course["category"]}')