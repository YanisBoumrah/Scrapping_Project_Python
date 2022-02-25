import requests
import json
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.46'}
    url = f'https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=Paris%20(75)&radius=10&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    for item in divs:
        title = item.find('h2', class_='jobTitle').get_text().strip()
        company = item.find('span', class_='companyName').text.strip()
        location = item.find('div', class_='companyLocation').get_text().strip()
        try:
            salary = item.find('div', class_='metadata salary-snippet-container').get_text().strip().replace('\xa0',
                                                                                                             '.')
        except:
            salary = ''
        summary = item.find('div', class_='job-snippet').get_text().strip()

        job = {
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
            'summary': summary

        }
        joblist.append(job)
    return


joblist = []
for i in range(0, 20, 10):
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist, columns=["title", "company", "location", "salary", "summary"])
df_json_dict = json.loads(df.to_json(orient = 'records'))
print(df_json_dict)

#for i in range(len(df_json_dict)):
    #requests.post('http://127.0.0.1:5000/jobs', json=df_json_dict[i])