# from celery import shared_task
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# @shared_task
# def scrape_coin_data(coin):
#     url = f"https://coinmarketcap.com/currencies/{coin}/"

#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')  # Run in headless mode for better performance
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')

#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
#     try:
#         driver.get(url)
#         price = driver.find_element(By.CLASS_NAME, "priceValue___11gHJ").text
#     except Exception as e:
#         driver.quit()
#         return {'error': str(e)}
    
#     driver.quit()
#     return {'coin': coin, 'price': price}
# # -*- coding: utf-8 -*-
from celery import shared_task
import requests
from bs4 import BeautifulSoup

@shared_task
def scrape_coin_data(coin):
    url = f"https://coinmarketcap.com/currencies/{coin}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find("div", class_="priceValue___11gHJ").text
    return {'coin': coin, 'price': price}

