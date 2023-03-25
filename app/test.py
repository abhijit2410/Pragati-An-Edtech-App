from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from imageDownloader import img_download
# from app.api import API
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from imageScraper import scrape_images

def scrape_text(query):
    print("Universal Scraping Started")
    URL = "https://www.google.co.in"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get(URL)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(query)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

    ele = driver.find_elements(By.XPATH,'//*[@id="exacc_GhuQY_KmLNegseMP29C2-AU_5"]/span')
    print(ele)
    page_source = driver.page_source.encode('utf8')
    soup = BeautifulSoup(page_source, 'lxml')


    related_list = []
    related_list.append('Related searches👇')
    related = soup.find_all(class_ = 's75CSd OhScic AB4Wff',limit=3)
    for x in related:
        related_list.append(x.get_text().strip())
    print(related_list)

    try:
        text1 = soup.find_all(class_ = 'bjV81b')
        text2 = soup.find_all(class_ = 'JDfRZb')
        driver.quit()
        if len(text1) == 0 or len(text2) == 0:
            raise Exception('List is empty')
        for a, b in zip(text1, text2):
            print(a.get_text(),b.get_text(),related_list)
            # api.template_queries(a.get_text(),b.get_text(),related_list)
            # related_list.clear()
            # del api
            return "null"
    except:
        try: # scraping all the lists from "People also ask"
            lists = []
            data = soup.find_all(class_ = 'TrT0Xe', limit=6)
            link = soup.find_all(class_ = 'truncation-information', limit=1)

            related = soup.find_all(class_ = 'iDjcJe IX9Lgd wwB5gf',limit=3)
            for x in related:
                related_list.append(x.get_text().strip())
            print(related_list)

            if len(data) == 0 or len(link) == 0:
                raise Exception('List is empty')

            for x in data:
                lists.append("▸ {}".format(x.get_text().strip()[:-1]))
            if len(link) != 0:
                lists.append("*For more* information, see {}".format(link[0].get("href")))
            concat = ''
            for each in lists:
                if each == lists[-1]:
                    concat += '\n'
                concat += each + '\n'
            lists.clear()   
            # driver.quit()
            # api.send_text(concat)
            time.sleep(3)
            print(concat)
            # api.template_related_searches(related_list)
            related_list.clear()
            # del api
            return "null"
        except:
            try: # scraping is done from "People also ask"
                data = soup.find_all(class_ = 'hgKElc', limit=1)
                print(data)
                img_url = scrape_images(query) # scrape related image
                print(img_url)

                related = soup.find_all(class_ = 'iDjcJe IX9Lgd wwB5gf',limit=3)
                for x in related:
                    related_list.append(x.get_text().strip())
                print(related_list)
                # driver.quit()
                # path = img_download(img_url)
            except:
                # driver.quit()
                print("Sorry couldn't find anything. I am still learning")
                return "null"

res = scrape_text('what is kmp algorithm')
# search = res[-1]
# for each in search: 
#         print(each)
# if type(res) == list:
#     for each in res: 
#         print(each)
# else:
#     print(res)