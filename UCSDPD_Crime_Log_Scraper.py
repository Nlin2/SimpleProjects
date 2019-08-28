import requests
from bs4 import BeautifulSoup

resp = requests.get('http://www.police.ucsd.edu/docs/reports/CallsandArrests/Calls_and_Arrests.asp')
soup = BeautifulSoup(resp.text, 'html.parser')
links = list(filter(lambda notEmpty: notEmpty, (map(lambda option: option["value"], soup.find_all("option")))))
i = 1
total = len(links)

for link in links:
    pdf_links = 'http://www.police.ucsd.edu/docs/reports/CallsandArrests/' + link.replace(' ', '%20')
    with open(link.split('/')[1], 'wb') as pdf:
        for chunk in requests.get(pdf_links):
            pdf.write(chunk)
        print(f'{i}/{total} Successful Download: {link.split("/")[1]}')
        i += 1
