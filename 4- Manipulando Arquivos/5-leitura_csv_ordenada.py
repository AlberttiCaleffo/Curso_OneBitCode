courses = []

with open('courses.csv', 'r', encoding= 'UTF-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        courses.append(f'{language} - {category}')
        print(courses)
        
for course in sorted(courses, reverse= True):
    print(course)