import requests
from bs4 import BeautifulSoup
import time

def getText(resp):
    soup = BeautifulSoup(resp.text, 'html.parser')
    content = soup.find('div', {'id': 'chapter-content'})
    s =  ''
    for p in content.find_all('p'):
        for attr in p():
            if attr.name == 'i':
                continue
            elif attr.name == 'span' or attr.name == 'a':
                if attr.get_text() == '\nNext Chapter\n' or attr.get_text() == '\nPrevious Chapter\n':
                    continue
                s += attr.get_text().strip() + ' '
            elif attr.name == 'hr':
                s += '______________________________________________________________________________'
        if p.name == 'p':
            s += '\n\n'
    return s.strip() + '\n', 'https://www.wuxiaworld.com' + content()[-1]['href']

firstChapterURL = input('First Chapter URL: ')
lastChapterURL = input("Last Chapter URL: ")
resp = requests.get(firstChapterURL)
fileName = input('File Name: ')
text, nextChapter = getText(resp)
with open(fileName, 'a') as f:
    while resp.status_code == 200 and lastChapterURL != nextChapter:
        time.sleep(1)
        text, nextChapter = getText(resp)
        f.write(text)
        resp = requests.get(nextChapter)
    if lastChapterURL == nextChapter:
        text, nextChapter = getText(resp)
        f.write(text)



