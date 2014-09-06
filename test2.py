import getPage
import bs4
def detail(link):
	print (link)
	try:
		chunk = getPage.get(link,3,'utf-8')
	except Exception:
		print ("Page Get Exception")
	
	content = ""
	soup = bs4.BeautifulSoup(chunk)
	div = soup.find('div',attrs = {'class':'context'})
	if div:
		for item in div.contents[2:-1]:
			content = content + str(item)
	print (content)

if __name__ == "__main__":
	link = 'http://www.lovebanker.com/bank/20130502/143.html'
	detail(link)
