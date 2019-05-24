import time
from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException





def main():
        driver = webdriver.Chrome()

        driver.get('https://shoferoff.ru/wp-admin/')
        time.sleep(1)
        login = driver.find_element_by_name("log")
        login.clear()
        login.send_keys('admin') 
        password = driver.find_element_by_name("pwd")
        password.clear()
        password.send_keys('insatb3493insatb3493')
        driver.find_element_by_name('wp-submit').click() 
        time.sleep(1)

        driver.get('https://shoferoff.ru/wp-admin/post-new.php')

        


if __name__ == '__main__':
        main()