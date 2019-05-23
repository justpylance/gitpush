import time
from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 


def csv_dict_reader(file_obj,cars):
    """
    Read a CSV file using csv.DictReader
    """

    reader = csv.DictReader(file_obj, delimiter=';')
    last_car =''
    for line in reader:
        
        line['Modification'].split('›')[0]
        if last_car != line['Modification'].split('›')[0]:
            cars.append(line['Modification'].split('›')[0][:-1])
        last_car =line['Modification'].split('›')[0]
        



def main(cr):
        driver = webdriver.Chrome()
        cars = []
        with open(str(cr.lower())+".csv") as f_obj:
                csv_dict_reader(f_obj,cars)
        print(cars)

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
        dwn_list = []

        for car in cars:
                dwn_dict = {'table_id_eq':'','car':car,'table_id_cmpl':''}
                equipment = ''
                complete = ''
                driver.get('https://shoferoff.ru/wp-admin/admin.php?page=tablepress&s='+car.replace(' ','+')) 
                time.sleep(1.5)
                html = driver.page_source
                soup = BeautifulSoup(html,'lxml')
                elems = soup.find('tbody',id='the-list').find_all('tr')
                try:
                    for tr in elems:
                            if 'оборудование ' + car.lower() == tr.find('td',class_='table_name').find('a').get_text().lower():
                                    dwn_dict['table_id_eq'] = tr.find('td', class_='table_id').get_text()
                            if 'комплектации и цены '+ car.lower() == tr.find('td',class_='table_name').find('a').get_text().lower():
                                    dwn_dict['table_id_cmpl'] = tr.find('td', class_='table_id').get_text()
                except:
                    pass
                dwn_list.append(dwn_dict)

        with open(str(cr)+'-'+'table_id'+'.csv','w')as file:
                writer = csv.writer(file, delimiter=';', lineterminator='\n')
                writer.writerow(('car','table_id_eq','table_id_cmpl'))
                for elem in dwn_list:
                	writer.writerow((elem['car'],elem['table_id_eq'],elem['table_id_cmpl']))










if __name__ == '__main__':
        cr = str(input('Раздел сайта(марка): '))
        main(cr)


