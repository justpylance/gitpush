import time
from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver





def get_car_urls(url):
        cars_urls=[]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        blocks = soup.find_all('div',class_='model_auto')
        for elem in blocks:
                url = 'http://carsdo.ru' + elem.find('a',class_='model_auto_a').get('href')
                
                cars_urls.append(url)
        return(cars_urls)

def get_complect(cars_urls,cars_options):
        cars_options = []

        
        for url in cars_urls[:2]:
                time.sleep(1)
                r = requests.get(url)
                soup = BeautifulSoup(r.text,'lxml')
                table_urls = []
                try:
                        mod_urls = soup.find('ul',id='complete').find_all('li')
                        for mod in mod_urls:
                                murl = 'http://carsdo.ru' +mod.find('a').get('href')
                                table_urls.append(murl)
                except:
                        pass

                for elem in table_urls[:1]:
                        car_dict = {}
                        r = requests.get(elem)
                        soup = BeautifulSoup(r.text, 'lxml')
                        car_dict['mod'] = soup.find('div',class_='block1').find('h1').get_text()
                        car_dict['table_id'] = ''
                        car_dict['url'] = ('https://shoferoff.ru/datsun/'+elem.split('audi/')[-1].split('/')[0] + car_dict['mod'].split('›')[-1]).replace(' ','-')
                        car_dict['title'] = car_dict['mod'].split('›')[0]
                        car_dict['description'] = soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[0].get_text() + ' ' +soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[1].get_text() 
                        car_dict['donor'] = elem
                        #car_dict['table_id'] = 
                        car_dict['price'] = soup.find('div',class_='price_kompl').find('span', class_='price_kompl_cena').get_text()
                        car_dict['packages']
                        lists = soup.find_all('ul', class_='komplektatsiya')

                        for ul in lists[:-1]:
                        #print(ul)
                            lis = ul.find_all('li')

                            more_inf += '<h3>'+ lis[0].get_text() + '</h3> <ul>'
                            if 'Пакеты' in str(lis[0]):
                                packages =  more_inf.replace('<ul>', '')
                                for li in lis[1:]:
                                    




                            
                            
                                            
                            for li in lis[1:]:
                                            #print(li)
                                more_inf += str(li)
                                more_inf += '</ul>'
                            print(more_inf)

                        cars_options.append(car_dict)
                        print('+')
                        #print(car_dict['price'])



                #print(murl)
        return cars_options


#def get_cars_options(cars_options,cars_urls):
        



def main():
        
        url = 'http://carsdo.ru/audi/'
        cars_urls = get_car_urls(url)
        
        cars_options = []
        cars_options = get_complect(cars_urls,cars_options)
        ###get_cars_options(cars_options,table_urls)

        '''
        driver = webdriver.Chrome()
        print(123)
        driver.get('https://shoferoff.ru/wp-admin/')
        time.sleep(1)
        login = driver.find_element_by_name("log")
        login.clear()
        login.send_keys('admin') 
        password = driver.find_element_by_name("pwd")
        password.clear()
        password.send_keys('insatb3493insatb3493')
        driver.find_element_by_name('wp-submit').click() 

        for car in cars_options:         
                time.sleep(1)
                driver.get('https://shoferoff.ru/wp-admin/admin.php?page=tablepress&s=audi')
        ''' 

        with open('BMW.csv','a+')as file:
                writer = csv.writer(file, delimiter=';', lineterminator='\n')
                writer.writerow(('Donor_Link','shoferoff_Link','Modification', 'Image_url', 'table_id','safe','design','interior' ,'price', 'packages', 'title', 'description' ))
                for elem in cars_options:
                        
                        writer.writerow((elem['donor'],elem['url'],elem['mod'], 'Image_url', 'table_id',elem['safe'],elem['design'] ,elem['interior'] , 'price', elem['packages'], elem['title'], elem['description'] ))
                        

               #.encode().decode('utf-8', 'ignore') 
                        


if __name__ == '__main__':
        main()
