import csv

import requests

from bs4 import BeautifulSoup




def create_table(complects):
	with open('output.csv','wb' , newline='') as f:
		writer = csv.writer(f,delimiter=';')
		writer.writerow(('title','description','category','price', 'characters','complects','imgs'))







def main():
	urls = [{'url':'https://www.harvey-rus.ru/catalog/cabinet-saws/','category':''}]

	for url in urls:
		soup = None
		soup = BeautifulSoup(requests.get(url['url']).text,'lxml')
		stans =[]

		stans = soup.find_all('div', class_='col-lg-3')
		category = url['category']
		for stan in stans:
			price = stan.find('div',class_='bx_catalog_item_price').get_text()

			title = stan.find('a').get_text()
			stan_url = 'https://www.harvey-rus.ru'+stan.find('a').get('href')
			imgs =[]

			soup=None
			soup = BeautifulSoup(requests.get(stan_url).text,'lxml')
			description =soup.find_all('div',class_='panel-default')[0].find('div',class_='panel-body').get_text()
			print(title)
			print(price)
			print(category)
			print(description)
			break


	complects = []


	#create_table(complects)







if __name__ == '__main__':
	main()