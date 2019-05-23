import csv
import time
import requests
from bs4 import BeautifulSoup

def getsoup(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')
        return soup

def getlist(soup):
        projs = soup.find('table', class_='table-normal').find_all('tr')[0]
        n_dict = {}
        n_dict['title'] = soup.find('td',class_='left').get_text().replace('\n','')
        n_dict['link'] = 'https://freelancehunt.com' +soup.find('td',class_='left').find('a').get('href')
        #print(n_dict)
        return(n_dict)


def csv_dict_reader(file_obj,):
        reader = csv.DictReader(file_obj, delimiter=';')
        
        x = 0
        
        for line in reader:
                title = ''
                link = str(line['Link'])
                try:
                        title = str(line['Title'])
                except: title = ''
                x+=1
                if x > 2:
                        break
        
        old = {'title': title, 'link':link}
        #print(old['link'])
        return old 




def main():
        while True:
                
                new =getlist(getsoup('https://freelancehunt.com/projects?skills%5B%5D=169'))
                with open("output1.csv") as f_obj:
                        new =getlist(getsoup('https://freelancehunt.com/projects?skills%5B%5D=169'))
                        old =csv_dict_reader(f_obj)
                
                
                        if str(old['link']) != new['link'] :
                                if 'парсер' in new['title'] or 'парсинга' in new['title'] or 'Парсинга' in new['title'] or 'Парсер' in new['title'] :
                                        print('send message')
                                        r = requests.post('https://sms.ru/sms/send?api_id=[E325F3FD-C904-4BCC-441E-925BDF6DD189]&to=79601198159&msg=''Найден+проект: '+str(new['link'])+'&json=1')
                                else:
                                	x = new['title'].split(' ')
                                	n = 0
                                	for j in x:
                                		if 'Парсинг' in j or 'парсинг' in j:
                                			n+=1
                                	if n>1:
                                		r = requests.post('https://sms.ru/sms/send?api_id=[E325F3FD-C904-4BCC-441E-925BDF6DD189]&to=79601198159&msg=''Найден+проект: '+str(new['link'])+'&json=1')


                                with open('output1.csv','w')as file:
                                        writer = csv.writer(file, delimiter=';', lineterminator='\n')
                                        writer.writerow(('Title','Link'))
                                        writer.writerow((str(new['title']),new['link']))
                        else:
                                pass#print('ne-a')
                time.sleep(100)

        



if __name__ == '__main__':
        main()
