import bs4, requests
import json
import io
import config


class Main:
	def __init__(self, session, soup):
		self.__session = session
		self.__soup = soup

class Session:
	def __init__(self, url):
		self.__session = requests.get(
			url,
			headers = config.headers
			)

	def get(self):
		return self.__session

class HTML:
	def __init__(self, soup):
		self.__soup = soup

	def get(self):
		return self.__soup

	def get_cryptos(self, count=1):
		soup = self.__soup
		for i in range(1,len(count)+1):
			crypto = soup.find(
				"table",
				{"class": "h7vnx2-2 czTsgW cmc-table  "}
			)
			print(crypto)



if __name__ == '__main__':
	Main(
		session = Session(
			url='https://coinmarketcap.com'
			)
		soup = HTML(
			html=bs4.BeautifulSoup(
				session.get().text,
				features="html.parser"
				)
			)
	)

