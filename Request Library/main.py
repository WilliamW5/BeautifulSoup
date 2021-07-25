from bs4 import BeautifulSoup
import requests
import time

# taking multiple inputs at a time
# and type casting using list() function
print("Insert a skill you are not familiar with: ")
unfamiliar_skill = list(map(str, input(">").split()))
print(f"Filtering out: {unfamiliar_skill}")

# Function which prints out Python jobs depending on unfamiliar skills
def job_finder():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    # find_all() pulls all tags (find() pulls the first tag)
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Enumerate through the jobs array, assigning index and job
    for index, job in enumerate(jobs):     
        published_date = job.find('span', class_='sim-posted').text.replace(' ', '')

        # Only posts if posted a few days ago will be printed
        if 'few' in published_date:
            # .replace() is used to fix the terrible formating
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')

            # Pulls the first header, h2, and a-tag: with href element
            link = job.header.h2.a['href']

            # For how many items you are unfamiliar with:
            for item in range(len(unfamiliar_skill)):
                if unfamiliar_skill[item] not in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f"Company Name: {company_name.strip()}\n")
                        f.write(f"Required Skills: {skills.strip()}\n")
                        f.write(f"Link: {link}\n")
            print(f"File saved: {index}")


if __name__ == '__main__':
    while True:
        job_finder()
        timer = 10
        print(f"Waiting {timer} minutes")
        time.sleep(timer * 60)