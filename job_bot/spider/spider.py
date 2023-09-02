import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response

class MySpider(scrapy.Spider):
    name = 'myspider'
    
    def start_requests(self):
        base_url = 'https://freelance.ru/project/search/pro?page={}&per-page=25'
        for i in range(1,3):
            yield scrapy.Request(url=base_url.format(i), callback=self.parse)
        
    
    def parse(self, response: Response):
        title = response.xpath('//*[@class="project-head"]/text()').get()
        if title:
            print("Title:", title)
        proj_links = response.xpath("//*[contains(concat(' ',normalize-space(@class),' '),' title ')]//a/@href").getall()
        if proj_links:
            for link in proj_links:
                yield response.follow(url=link, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0',
        'LOG_ENABLED': True
    })
    process.crawl(MySpider)
    process.start()