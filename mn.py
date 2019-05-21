import requests
from bs4 import BeautifulSoup

r = requests.get('http://carsdo.ru/audi/q8/')

soup = BeautifulSoup(r.text,'lxml')

urls = soup.find('table', id='price').find_all('a')

for url in urls:
	#print(url)
	r = requests.get('http://carsdo.ru'+url.get('href'))
	soup = BeautifulSoup(r.text,'lxml')
	more_inf = ''
	lists = soup.find_all('ul', class_='komplektatsiya')

	for ul in lists[:-1]:
		#print(ul)
		lis = ul.find_all('li')
		more_inf += '<h3>'+ lis[0].get_text() + '</h3> <ul>' 
		for li in lis[1:]:
			#print(li)
			more_inf += str(li)
		more_inf += '</ul>'
	print(more_inf)
	break
