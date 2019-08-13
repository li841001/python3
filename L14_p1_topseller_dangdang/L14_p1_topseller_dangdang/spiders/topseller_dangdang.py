import scrapy,bs4
from ..items import L14P1TopsellerDangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'Dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for i in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%d'%i
        start_urls.append(url)
        def parse(self, response):
            soup = bs4.BeautifulSoup(response.text,'html.parser')
            datas = soup.find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
            for data in datas:
                item = L14P1TopsellerDangdangItem()
                item['book_name'] = data.find(class_='name').find('a')['title']
                item['writer'] = data.find_all(class_='publisher_info')[0].find('a')['title']
                item['price'] = data.find(class_='price_n').text
                print('%s\n%s\n%s\n---'%(item['book_name'],item['writer'],item['price']))
                yield item