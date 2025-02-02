import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield{
                'name':book.css('h3 a::text').get(),
                'price':book.css('div.product_price .price_color::text').get(),
                'url':book.css('h3 a').attrib['href']
            }


        
