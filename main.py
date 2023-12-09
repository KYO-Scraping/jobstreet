import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.jobstreet.co.id/id/data-jobs/in-Bali'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/120.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers)

#print(res.status_code)
#print(soup.prettify())

def get_total_pages():
    res = requests.get(url, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+', encoding='utf-8') as outfile:
        outfile.write(res.text)
        outfile.close()

    #Scraping
    soup = BeautifulSoup(res.text, 'html.parser')

    pagination = soup.find('ul', '_1wkzzau0 _1wkzzau3 a1msqi5a a1msqifq')
    pages = pagination.find_all('li')

    total_pages = []
    for page in pages:
        if(page.text.isdigit()):
            total_pages.append(page.text)

    total = int(max(total_pages))
    return total

if __name__ == '__main__':
    get_total_pages()