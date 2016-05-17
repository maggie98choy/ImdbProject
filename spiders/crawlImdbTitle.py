from scrapy.spiders import CrawlSpider, Rule
from ImdbProject.items import ImdbprojectItem
from scrapy.selector import Selector
from lxml import html
from scrapy.linkextractors import LinkExtractor

class ImdbSpider(CrawlSpider):
    name = "ImdbAllMovies"
    allowed_domains = ["imdb.com"]
    
    start_urls = ["http://www.imdb.com/search/title?year=%d,%d&title_type=feature&sort=moviemeter,asc" %(n,n) for n in range(1874, 2027)]
    rules = Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[@id="right"]/span[@class="pagination"]/a')),callback='parse_items',follow=True),


    def parse_items(self, response):
        hxs = Selector(response)
        items = []
        item = ImdbprojectItem()
        results = hxs.select('//td[@class="title"]')
    
        for result in results:
            item['title'] = result.select('a/text()').extract()
            item['year'] = result.select('span[@class="year_type"]/text()').extract()
            user_rating_value = result.select('div[@class="user_rating"]/div[@class="rating
            rating-list"]/span[@class="rating-rating"]/span[@class="value"]/text()').extract()
            item['user_rating'] = user_rating_value
            credit = result.select('span[@class="credit"]').xpath('a[contains(@href,"name")]/text()').extract()
            item['credit'] = credit
            item['outline'] = result.select('span[@class="outline"]/text()').extract()
            yield item