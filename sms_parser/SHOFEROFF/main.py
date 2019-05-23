import time
from bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver


cars = 'audi'


def get_car_urls(url):
        cars_urls=[]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        blocks = soup.find_all('div',class_='model_auto')
        for elem in blocks:
                url = 'http://carsdo.ru' + elem.find('a',class_='model_auto_a').get('href')
                
                cars_urls.append(url)
        return(cars_urls)

def get_complect(cars_urls,cars_options,cr):
        cars_options = []

        
        for url in cars_urls:
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

                for elem in table_urls:
                        car_dict = {}
                        r = requests.get(elem)
                        soup = BeautifulSoup(r.text, 'lxml')
                        
                        car_dict['mod'] = soup.find('div',class_='block1').find('h1').get_text()
                        car_dict['table_id'] = ''
                        print(car_dict['mod'])
                        car_dict['url'] = ('https://shoferoff.ru/'+str(cr)+'/'+elem.split(str(cr)+'/')[-1].split('/')[0] + car_dict['mod'].split('›')[-1]).replace(' ','-')
                        car_dict['title'] = car_dict['mod'].split('›')[0]
                        car_dict['description'] = soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[0].get_text() + ' ' +soup.find('div', class_='table_eq').find_all('div')[0].find('a').find_all('span')[1].get_text() 
                        car_dict['donor'] = elem
                        #car_dict['table_id'] = 
                        car_dict['price'] = soup.find('div',class_='price_kompl').find('span', class_='price_kompl_cena').get_text().encode('utf-8').decode()
                        
                        lists = soup.find_all('ul', class_='komplektatsiya')



                        car_dict['safe'] = ''
                        car_dict['design'] = ''
                        car_dict['interior'] = ''
                        car_dict['packages'] = ''
                        for ul in lists:
                        #print(ul)
                            lis = ul.find_all('li')
                            if 'Безопасность' in str(lis[0]):
                                safe =  '<h3>' + lis[0].get_text() + '</h3><ul>'
                                for li in lis[1:]:
                                        
                                        safe+= '<li>' + li.get_text()+'</li>'
                                safe+='</ul>'
                                car_dict['safe'] = safe.replace('（', '(').replace('）',')').replace('×','')#.encode('utf-8').decode() #('cp1251').decode("utf-8", "ignore")  #   'Дизайн'

                            if 'Дизайн' in str(lis[0]):
                                design =  '<h3>' + lis[0].get_text() + '</h3><ul>'
                                
                                for li in lis[1:]:
                                                
                                        '''except:
                                                print('+++')'''
                                        
                                        
                                        design+= '<li>' + li.get_text()+'</li>'
                                design+='</ul>'
                                car_dict['design'] = design.replace('（', '(').replace('）',')').replace('×','')#.encode('utf-8').decode()#('cp1251').decode("utf-8", "ignore") #Интерьер 
                            if 'Интерьер' in str(lis[0]):
                                interior =  '<h3>' + lis[0].get_text() + '</h3><ul>'
                                for li in lis[1:]:
                                        interior+= '<li>' + li.get_text()+'</li>'
                                interior+='</ul>'
                                car_dict['interior'] = interior.replace('（', '(').replace('）',')').replace('×','')#.encode('utf-8').decode()#('cp1251').decode("utf-8", "ignore") #Интерьер
                        
                        



                            

                            
                            if 'Пакеты' in str(lis[0].get_text()):

                                    packages =  '<h3>' + lis[0].get_text() + '</h3>'
                                    for li in lis[1:]:
                                                #if len(li.find_all('span'))
                                            if ':' in li.get_text():
                                                packages+=' [su_service title=\"'+   str(li.get_text()).replace(str(li.find('span',class_='dop_price').get_text()),'').split(':')[0]  +'\" icon="icon: plus-circle" icon_color="#ffd64f"] ' +  ' [/su_service]'  # '[su_note note_color="#fff9d4"]280 000 руб.[/su_note]'
                                                pack =  str(li.get_text()).replace(str(li.find('span',class_='dop_price').get_text()),'').split(':')[-1].split('+')
                                                packages += '<ul>'
                                                for p in pack:
                                                        packages += '<li>' + str(p) +'</li>'
                                                packages+='</ul>'
                                                packages += '[su_note note_color="#fff9d4"]' + li.find('span',class_='dop_price').get_text() +'[/su_note]'
                                                #.encode('cp1251')
                                                
                                                

                                            else:
                                                packages+= ' [su_service title=\"'+str(li.get_text()).replace(str(li.find('span',class_='dop_price').get_text()),'')  +'\" icon="icon: plus-circle" icon_color="#ffd64f"] '  +  ' [/su_service]' + '[su_note note_color="#fff9d4"]' + li.find('span',class_='dop_price').get_text() +'[/su_note]'
                                    car_dict['packages'] = packages.replace('（', '(').replace('）',')').replace('×','')
                                    #print(car_dict['packages'])
                                    
                                        


                                    




                            
                            
                                            
                            
                            

                        cars_options.append(car_dict)
                        #print('+')
                        #print(car_dict['price'])



                #print(murl)
        return cars_options


#def get_cars_options(cars_options,cars_urls):
        



def main(cr):
        
        url = 'http://carsdo.ru/'+str(cr) +'/'
        cars_urls = get_car_urls(url)
        
        cars_options = []
        cars_options = get_complect(cars_urls,cars_options,cr)
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

        with open(str(cr)+'.csv','a+')as file:
                writer = csv.writer(file, delimiter=';', lineterminator='\n')
                writer.writerow(('Donor_Link','shoferoff_Link','Modification', 'Image_url', 'table_id','safe','design','interior' ,'price', 'packages', 'title', 'description' ))
                for elem in cars_options:
                        try:
                                writer.writerow((elem['donor'],elem['url'],elem['mod'], 'Image_url', 'table_id',elem['safe'],elem['design'] ,elem['interior'] , elem['price'], elem['packages'], elem['title'], elem['description'] ))
                        except:
                                print('error csv')
                                '''print(elem['donor'])
                                writer.writerow((elem['safe']))
                                print(elem['design'])
                                
                                for x in elem['design']:
                                        try:
                                                writer.writerow((x))
                                        except:
                                                print(x)
                                '''
               #.encode().decode('utf-8', 'ignore') 
                        


if __name__ == '__main__':
        main(cars.lower())
