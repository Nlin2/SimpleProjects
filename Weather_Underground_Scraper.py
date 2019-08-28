from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import datetime

START = "https://api.wunderground.com"
END = "?req_city=Boston&req_state=MA&reqdb.zip=02115&reqdb.magic=1&reqdb.wmo=99999"

# Year/Month/Day
START_DATE = '/history/airport/KBOS/2012/1/1/DailyHistory.html'
STOP_DATE = '/history/airport/KBOS/2019/7/13/DailyHistory.html'

def toDate(time, date):
    M_to_Num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, 
                "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    hour = -1
    minute = -1
    month = -1
    day = -1
    year = -1
    
    # Time
    time, meridiem = time.split(" ")
    if meridiem == "AM":
        hour, minute = (int(val) for val in time.split(":"))
    else:
        hour, minute = (int(val) for val in time.split(":"))
        hour += 12
    
    # Date
    date = date.split(',')[1:3]
    month, day = date[0].split()
    month = M_to_Num[month]
    day = int(day)
    year = int(date[1])
    
    # 0 - 23 for hour
    return datetime.datetime(year, month, day, hour - 1, minute, 0, 0)
    
def htmlTableToDF(table, date):
    output_rows = []
    headers = []
    
    # header
    for header in table.find_all('th'):
        if header.text == 'Time (EDT)':
            headers.append('Time (EST)')
        else:
            headers.append(header.text)
    
    # rows
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text.strip('\n').strip('\t').strip('-').strip('N/A'))
        output_rows.append(output_row)
    
    df = pd.DataFrame(output_rows[1:], columns=headers)
    df["Time (EST)"] = df["Time (EST)"].map(lambda time: toDate(time, date))
    return df
# Intializations
url = START + START_DATE + END
html = urlopen(url).read()
soup = BeautifulSoup(html)
current_date = soup.find('a', text= "Next Day »")["href"]
url = START + current_date + END
df = htmlTableToDF(soup.find(id='obsTable'), soup.find('h2', class_='history-date').text)

while True:
    print(current_date)
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    current_date = soup.find('a', text= "Next Day »")["href"]
    url = START + current_date + END
    if current_date == STOP_DATE:
        print("COMPLETE")
        break
    try:
        df = df.append(htmlTableToDF(soup.find(id='obsTable'), soup.find('h2', class_='history-date').text), ignore_index=True)
    except AttributeError: # for missing days
        print("MISSING DATE: " + current_date)
        continue
