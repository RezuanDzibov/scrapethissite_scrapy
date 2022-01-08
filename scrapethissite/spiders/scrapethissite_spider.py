import scrapy
from scrapy.selector import Selector

from scrapethissite.items import ScrapethissiteHockeyItem, ScrapethissiteCountryItem


class ScrapethissiteHockeySpider(scrapy.Spider):
    name = 'scrapethissite_hockey'
    start_urls = ['https://www.scrapethissite.com/pages/forms/?&per_page=100']
    headers = [
        'name', 
        'year', 
        'wins', 
        'losses', 
        'ot_losses', 
        'pct', 
        'gf', 
        'ga',
        'diff'
    ]
    
    def parse(self, response, **kwargs):
        rows = response.css('tr.team')
        for row in rows:
            item = ScrapethissiteHockeyItem()
            row_tds = list([td.strip() for td in row.css(f'td::text').getall()])
            for header, td in zip(self.headers, row_tds):
                item[f'{header}'] = td
            yield item
        for next_page in response.xpath('/html/body/div[1]/section/div/div[5]/div[1]/ul/li[7]/a'):
                yield response.follow(next_page, self.parse)
                

class ScrapethissiteCountriesSpider(scrapy.Spider):
    name = 'scrapethissite_countries'
    start_urls = ['https://www.scrapethissite.com/pages/simple/']
    headers = ['country-name', 'country-capital', 'country-population', 'country-area']
    
    def parse(self, response, **kwargs):
        rows = response.css('div.country').getall()
        for row in rows:
            item = ScrapethissiteCountryItem()
            row = Selector(text=row)
            for header in self.headers:
                if header == 'country-name':
                    item[f"{header.replace('-', '_')}"] = row.xpath('//h3//text()').extract()[1].strip()
                    continue
                item[f"{header.replace('-', '_')}"] = row.css(f'span.{header}::text').get().strip()
            yield item