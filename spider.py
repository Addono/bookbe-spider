import scrapy

URL = "https://www.boek.be/zoek/boek/?e=1&genre=&archief=0&productvorm=papierenboeken%2Cebooks%2Cluisterboeken%2Coverigeboeken"

class Spider(scrapy.Spider):
    name = 'boek-be'
    start_urls = [URL]

    def parse(self, response):
        for title in response.css('.title ::text').extract():
            yield {"title:": title}

        for next_page in response.css('.item-list-pager a'):
           yield response.follow(next_page, self.parse)
