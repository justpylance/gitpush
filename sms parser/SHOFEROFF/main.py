import time
from bs4 import BeautifulSoup
import csv
import requests




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

        
        for url in cars_urls:
                time.sleep(3)
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

                for elem in table_urls:
                        car_dict = {}
                        r = requests.get(elem)
                        soup = BeautifulSoup(r.text, 'lxml')
                        car_dict['mod'] = soup.find('div',class_='block1').find('h1').get_text()
                        car_dict['url'] = ('https://shoferoff.ru/bmw/'+elem.split('bmw/')[-1].split('/')[0] + car_dict['mod'].split('›')[-1]).replace(' ','-')
                        car_dict['title'] = car_dict['mod'].split('›')[0]
                        car_dict['description'] = soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[0].get_text() + ' ' +soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[1].get_text() 
                        car_dict['safe'] = str(soup.find_all('ul',class_='komplektatsiya')[0])
                        car_dict['design'] = str(soup.find_all('ul', class_='komplektatsiya')[1])
                        car_dict['interior'] =  str(soup.find_all('ul', class_='komplektatsiya')[2])
                        car_dict['donor'] = elem
                        #car_dict['table_id'] = 
                        car_dict['price'] = soup.find('div',class_='price_kompl').find('span', class_='price_kompl_cena').get_text()
                        car_dict['packages'] = ''
                        packages = soup.find_all('ul',class_='komplektatsiya')[-1]#.find_all('li',class_='dop')
                        try:
                                if packages.get_text().count('Пакеты') >=1:
                                        packages = packages.find_all('li',class_='dop')
                        
                                        for pack in packages:
                                                if pack.find('span',class_='dop_obor').get_text().count(':') == 1:
                                                        pack = '[su_service title="'+pack.find('span',class_='dop_obor').get_text().split(':')[0].replace('\"','')  +'" icon="icon: plus-circle" icon_color="#ffd64f"][/su_service][su_note note_color="#fff9d4"]'+pack.find('span',class_='dop_price').get_text()+'[/su_note]'
                                                        car_dict['packages']+= pack + ' '
                                                        
                                                else:
                                                        pack ='[su_service title="'+pack.find('span',class_='dop_obor').get_text().replace('\"','')  +'" icon="icon: plus-circle" icon_color="#ffd64f"][/su_service][su_note note_color="#fff9d4"]'+pack.find('span',class_='dop_price').get_text()+'[/su_note]' 
                                                        #print(pack)
                                                        car_dict['packages']+= pack + ' '
                        except:                 
                                pass
                        cars_options.append(car_dict)
                        print('+')
                        #print(car_dict['price'])



                #print(murl)
        return cars_options


#def get_cars_options(cars_options,cars_urls):
        



def main():
        url = 'http://carsdo.ru/bmw/'
        cars_urls = get_car_urls(url)

        cars_options = []
        cars_options = get_complect(cars_urls,cars_options)
        #get_cars_options(cars_options,table_urls)
        with open('BMW.csv','a+')as file:
                writer = csv.writer(file, delimiter=';', lineterminator='\n')
                writer.writerow(('Donor_Link','shoferoff_Link','Modification', 'Image_url', 'table_id','safe','design','interior' ,'price', 'packages', 'title', 'description' ))
                for elem in cars_options:
                        writer.writerow((elem['donor'],elem['url'],elem['mod'], 'Image_url', 'table_id',elem['safe'],elem['design'],elem['interior'], elem['price'], elem['packages'], elem['title'], elem['description'] ))

                
                        


if __name__ == '__main__':
        main()
