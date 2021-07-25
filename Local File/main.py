from bs4 import BeautifulSoup

# pip install lxml, requests, beautifulsoup4
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        # sets equal to all h5-text in course
        course_name = course.h5.text

        # splits the text into an array and [-1] = last element in array
        course_price = course.a.text.split()[-1]

        # example of f-string
        print(course_name + ' costs ' + course_price)
        print(f'{course_name} costs {course_price}')