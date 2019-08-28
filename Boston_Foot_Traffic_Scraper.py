from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import requests
import os
import time

driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get('https://sceris.cityofboston.gov/sceriswebbtd/client/SearchResultsX.aspx?SearchParams=%3cSearchParms+xmlns%3axsi%3d%22http%3a%2f%2fwww.w3.org%2f2001%2fXMLSchema-instance%22+xmlns%3axsd%3d%22http%3a%2f%2fwww.w3.org%2f2001%2fXMLSchema%22%3e%3cFolderIDs%3e%3cint%3e56%3c%2fint%3e%3c%2fFolderIDs%3e%3cCriteria%3e%3cCr+N%3d%22Site+Location%22+V%3d%229999%22+CompOpr%3d%22LE%22+%2f%3e%3c%2fCriteria%3e%3cUdiDisplayNamesToDisp%3e%3cD+N%3d%22Intersection+Number%22+%2f%3e%3cD+N%3d%22Associated+Streets%22+%2f%3e%3cD+N%3d%22Collection+Date%22+%2f%3e%3cD+N%3d%22Data+Type%22+%2f%3e%3cD+N%3d%22Neighborhood+Code%22+%2f%3e%3cD+N%3d%22Site+Location%22+%2f%3e%3cD+N%3d%22Street+Name%22+%2f%3e%3cD+N%3d%22Study+Period%22+%2f%3e%3cD+N%3d%22Study+Type%22+%2f%3e%3c%2fUdiDisplayNamesToDisp%3e%3c%2fSearchParms%3e')

viewButton = driver.find_element_by_id("Submit")

for i in range(1000, 1500):
    #actions = webdriver.common.action_chains.ActionChains(driver)

    element = driver.find_element_by_id(i)

    element.click()
    time.sleep(3)
    viewButton.click()
    time.sleep(3)
    element.click()
    try:
        driver.switch_to.window(driver.window_handles[1])
        r = requests.get(driver.current_url, stream=True)
        with open(f'./traffic/{i}.pdf', 'wb') as fd:
            for chunk in r.iter_content(2000):
                fd.write(chunk)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except IndexError:
        pass
    finally:
        #actions.perform()
        print("Success: " + str(i))
