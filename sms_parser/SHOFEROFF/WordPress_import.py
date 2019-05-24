import time
from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def csv_dict_reader_id(file_obj,table_id):
    """
    Read a CSV file using csv.DictReader
    """
    table_id = []
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        table_id.append({'name':line['car'], 'table_id_eq':line['table_id_eq'],'table_id_cmpl':line['table_id_cmpl'] })
        #print({'name':line['car'], 'table_id_eq':line['table_id_eq'],'table_id_cmpl':line['table_id_cmpl'] })
        
        
def csv_dict_reader_cars(file_obj,cars):
    """
    Read a CSV file using csv.DictReader
    """
    cars = []
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        Donor_Link = line['Donor_Link']
        shoferoff_Link = line['shoferoff_Link']
        mod = line['Modification']
        img = line['Image_url']
        table_id=line['table_id']
        safe = line['safe']
        design = line['design']
        interior = line['interior']
        price = line['price']
        packages = line['packages']
        title = line['title']
        description = line['description']
        crdict = {}
        crdict = {'Donor_Link':Donor_Link,'shoferoff_Link':shoferoff_Link,'mod':mod,'img':img,'table_id':table_id,'safe':safe,'design':design,'interior':interior,'price':price,'packages':packages,'title':title,'description':description}
        cars.append(crdict)
        print(crdict)
        break
     



def main(cr):
        

        table_id = []
        try:
                with open(str(cr)+'-'+'table_id'+'.csv') as f_obj:
                    csv_dict_reader_id(f_obj,table_id)
        except:
            print(' \nФайла '+str(cr)+'-'+'table_id'+'.csv'+' не существует или возникла ошибка при переборе ячеек.\nЗапустите'+' table_id.py и после выполнения программы запустите программу заново \n')
            
        cars = []

        with open(str(cr)+'.csv') as f_obj:
                csv_dict_reader_cars(f_obj,cars)

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
        cr = str(input('Загрузка машин марки: '))
        main(cr)

        

        
