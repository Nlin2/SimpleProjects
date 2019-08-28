import requests
import urllib
from bs4 import BeautifulSoup
import os

resp = requests.get(input("Please Insert Podcast Link: "))
soup = BeautifulSoup(resp.text, 'html.parser')
class_name = ''.join(soup.find(id='title_Label').text.split()[:2])
if (not os.path.exists(class_name)):
    os.mkdir(class_name)


all_lecture_links = list(map(lambda a: a["href"], soup.find_all('a', {'class': ['other-media video match', 'current-media video match']})))
i = 1
total_downloads = len(all_lecture_links)

for link in all_lecture_links:
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'html.parser')
    download = requests.get('https://podcast.ucsd.edu' + soup.find(class_='DownloadLink')["href"], stream=True)
    lecture_name, date = soup.find("div", {"id": "LectureHeader"}).h2.text.split(',')
    full_name = f'{class_name}/{class_name}_{lecture_name.replace(" ", "_")}_{date.replace(" ", "").replace("/", "-")}.mp4'
    with open(full_name, "wb") as mp4file:
        for chunk in download.iter_content(chunk_size = 1024):
            if chunk:
                mp4file.write(chunk)
        print(f"{i}/{total_downloads} Download Complete: {full_name}")
    i += 1
