import csv

import requests

from bs4 import BeautifulSoup












def main():
	urls = ['https://www.harvey-rus.ru/catalog/cabinet-saws/']

	for url in urls:
		soup = None
		soup = BeautifulSoup(requests.get(url).text,'lxml')
		stans =[]
		stans = soup.find_all('div', class_='col-lg-3')
		for stan in stans:
			print('https://www.harvey-rus.ru'+stan.find('a').get('href'))


	complects = []







if __name__ == '__main__':
	main()