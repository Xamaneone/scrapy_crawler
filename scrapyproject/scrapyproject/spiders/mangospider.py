import scrapy
from scrapy_selenium import SeleniumRequest

class MangospiderSpider(scrapy.Spider):
    name = 'mangospider'


    def start_requests(self):
        yield SeleniumRequest(
            url="http://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99",
            callback=self.parse,
            wait_time=3
        )

    
    def parse(self, response):
        selected_color_div = str(response.css("div.color-container--selected").get())

        price = float(response.xpath('//meta[@itemprop="price"]/@content').get())

        all_size = response.css("span::attr(data-size)").getall()
        all_size.pop(0)

        
        yield {
            'name': str(response.css('h1::text').get()),
            'price': price,
            'color': str(selected_color_div[17::].split(' ')[0]),
            'size': all_size
        }