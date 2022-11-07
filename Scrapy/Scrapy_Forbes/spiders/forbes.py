import scrapy


class ForbesSpider(scrapy.Spider):
    name = 'forbes'
    start_urls = ['https://www.forbes.com/lists/global2000/?sh=216e8b3c5ac0']

    def parse(self, response):
        for empresa in response.css('.table-row'):
            yield {
                'rank': empresa.css('.rank::text').get()[:-1],
                'empresa': empresa.css('.name::text').get(),
                'pais': empresa.css('.country::text').get(),
                'sales': empresa.css('.sales::text').get(),
                'profit': empresa.css('.profit::text').get(),
                'market_value': empresa.css('.value::text').get(),
            }

