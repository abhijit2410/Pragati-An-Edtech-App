from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Define the path to chrome driver


def _build_query(query:str):
    return f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"

def _get_info(query):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument(f'user-agent={user_agent}')

        wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        # This searches images from google.com
        wd.get('https://google.com')
        # image_urls = set()

        wd.get(_build_query(query))

        # img.Q4LuWd is the google tumbnail selector
        thumbnails = wd.find_elements(by=By.CSS_SELECTOR, value="img.Q4LuWd")

        for img in thumbnails[0:10]:
            # We need to click every thumbnail so we can get the full image.
            try:
                img.click()
            except Exception:
                print('ERROR: Cannot click on the image.')
                continue

            images = wd.find_elements(by=By.CSS_SELECTOR, value='img.n3VNCb')
            time.sleep(0.2)

            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    # image_urls.add(image.get_attribute('src'))
                    image_url = image.get_attribute('src')
                    if image_url == None:
                        continue
                    else:
                        wd.quit()
                        return image_url


def scrape_images(query):
    image_info = _get_info(query)
    return image_info

# url = scrape_images('what is depth first search')
# print(url)

