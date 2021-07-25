from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    
    # returns all h5 in an list format
    courses_html_tags = soup.find_all('h5')
    # prinmts the text in the existing html tags
    for course in courses_html_tags:
        print(course.text)
    