import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.jobstreet.co.id/id/data-jobs/in-Bali'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/120.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
base_link = 'https://www.jobstreet.co.id'
job_list = []

# print(res.status_code)
# print(soup.prettify())


# Function to get pages quantity
def get_total_pages():
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+', encoding='utf-8') as outfile:
        outfile.write(res.text)
        outfile.close()

    # Scraping
    soup = BeautifulSoup(res.text, 'html.parser')

    pagination = soup.find('ul', '_1wkzzau0 _1wkzzau3 a1msqi5a a1msqifq')
    pages = pagination.find_all('li')

    total_pages = []
    for page in pages:
        if (page.text.isdigit()):
            total_pages.append(page.text)

    total = int(max(total_pages))
    return total

# Function to get all items
def get_all_items():
    with open('temp/res.html', 'w+', encoding='utf+8') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    # Scraping
    parent01 = soup.find_all('article', '_1wkzzau0 _1wkzzau1 a1msqi7i a1msqi6e a1msqi9q a1msqi8m a1msqi66 a1msqih a1msqi5e uo6mkb a1msqi4i a1msqi4b lnocuo18 lnocuo1b a1msqi32 a1msqi35')

    for items in parent01:
        jobTitle = items.find('h3', '_1wkzzau0 a1msqi4y lnocuo0 lnocuol _1d0g9qk4 lnocuov lnocuo21').text
        companyName = items.find('span', '_1wkzzau0 a1msqi4y lnocuo0 lnocuo1 lnocuo21 _1d0g9qk4 lnocuoa').text[3:]
        jobLocation = items.find('span', '_1wkzzau0 a1msqi4y lnocuo0 lnocuo1 lnocuo21 _1d0g9qk4 lnocuo7').text

        sR = items.find('span', '_1wkzzau0 _16v7pfz1 a1msqi4y a1msqi0 a1msqir _16v7pfz3')
        try:
            salaryRange = str(sR)[91:len(str(sR))-7]
        except:
            salaryRange = 'Salary Range is not available'
        if(salaryRange==''):
            salaryRange = 'Salary Range is not available'

        cL = items.find('span', '_1wkzzau0 a1msqi4y lnocuo0 lnocuo1 lnocuo21 _1d0g9qk4 lnocuoa')
        checkLink = int(str(cL).find('href="'))
        if(checkLink!=-1):
            str01 = str(cL)[checkLink+6:]
            companyLink = base_link + str01[0:int(str01.find('"'))]
        else:
            companyLink = 'Company Link is not available'

        data_dictionary = {
            'Job Title': jobTitle,
            'Company Name': companyName,
            'Job Location': jobLocation,
            'Salary Range': salaryRange,
            'Company Link': companyLink
        }

        job_list.append(data_dictionary)

    print(job_list[0])




if __name__ == '__main__':
    get_all_items()
