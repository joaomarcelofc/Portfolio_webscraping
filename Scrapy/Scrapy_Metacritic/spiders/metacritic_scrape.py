import scrapy


class MetacriticScrapeSpider(scrapy.Spider):
    name = 'metacritic'
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/all/all/filtered']

    def parse(self, response):
        for game in response.css('.clamp-summary-wrap'):
            yield {
                'game': game.css('.title h3::text').get(),
                'plataforma': game.css('.platform .data::text').get().strip(),
                'data_lcto': game.css('.platform+ span::text').get(),
                'score':  game.css('.clamp-score-wrap .metascore_w::text').get()
            }

        next_page = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "action", " " ))]').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

