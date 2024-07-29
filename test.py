profile_path = '/browser_profile/yh9n45l8.SeleniumProfile'

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

firefox_options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
firefox_options.set_preference("general.useragent.override", user_agent)

firefox_options.set_preference('profile', profile_path)

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)


def random_delay(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))


def emulate_scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    random_delay(1, 2)
    driver.execute_script("window.scrollTo(0, 0);")
    random_delay(1, 2)


url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
driver.get(url)
random_delay(3, 5)

emulate_scroll()

ads = driver.find_elements(By.CSS_SELECTOR, 'div.bull-item')[:10]

ad_list = []

for ad in ads:
    ad_id = ad.get_attribute('data-bulletin-id')

    description_cell = ad.find_element(By.CSS_SELECTOR,
                                       'div.descriptionCell.bull-item__cell.bull-item__description-cell')

    title_tag = description_cell.find_element(By.CSS_SELECTOR, 'a.bulletinLink')
    title = title_tag.text.strip()

    views_count_tag = description_cell.find_element(By.CSS_SELECTOR, 'span.views')
    views_count = views_count_tag.text.strip()

    position = ads.index(ad) + 1

    ad_link = title_tag.get_attribute('href')
    driver.get(ad_link)
    random_delay(3, 5)

    emulate_scroll()

    author_tag = driver.find_element(By.CSS_SELECTOR, 'div.viewbull-summary__seller .userNick a')
    author_name = author_tag.text.strip()
    author_link = author_tag.get_attribute('href')

    city_tag = driver.find_element(By.CSS_SELECTOR, 'div.viewbull-summary__seller .seller-summary div:nth-child(4)')
    city = city_tag.text.strip() if city_tag else "N/A"

    driver.back()
    random_delay(3, 5)

    ad_data = {
        'title': title,
        'ad_id': ad_id,
        'views_count': views_count,
        'position': position,
        'author_name': author_name,
        'author_link': author_link,
        'city': city
    }

    ad_list.append(ad_data)

for ad in ad_list:
    print(ad)

driver.quit()
