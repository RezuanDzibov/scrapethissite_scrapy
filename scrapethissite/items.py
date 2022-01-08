# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapethissiteHockeyItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    wins = scrapy.Field()
    losses = scrapy.Field()
    ot_losses = scrapy.Field()
    pct = scrapy.Field()
    gf = scrapy.Field()
    ga = scrapy.Field()
    diff = scrapy.Field()


class ScrapethissiteCountryItem(scrapy.Item):
    country_name = scrapy.Field()
    country_capital = scrapy.Field()
    country_population = scrapy.Field()
    country_area = scrapy.Field()