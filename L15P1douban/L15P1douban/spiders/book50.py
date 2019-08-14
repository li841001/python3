import scrapy,bs4
from ..items import L15P1DoubanItem

class Book_50(scrapy.Spider):
    name = 'books'
    allowed_domain = ['book.douban.com']
    start_urls = []
    for i in range(0,50,25):
        url = 'https://book.douban.com/top250?start=%d'%i
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        url_list = soup.find('div',class_='article').find_all('table')
        for url in url_list:
            final_url = url.find('a')['href']+'comments/'
            yield scrapy.Request(final_url,callback=self.parse_job)

    def parse_job(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        c_list = soup.find_all('li',class_='comment-item')
        book_name = soup.find('div',id='content').find('h1').text.replace(' 短评','')
        for c_item in c_list:
            item = L15P1DoubanItem()
            item['book_name'] = book_name
            item['cid'] = c_item['data-cid']
            item['c_content'] = c_item.find('span',class_='short').text
            item['c_reader'] = c_item.find(class_='comment-info').find('a').text
            yield item