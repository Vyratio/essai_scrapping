import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule




class MonCrawlSpiderSpider(CrawlSpider):
    name = 'mon_crawl_spider'
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    start_urls = ['https://www.imdb.com/chart/top/']

    rules=(
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'),callback='parse_item',follow =True),
    )

    def parse_item(self,response):
        
        yield{
            'Nom du film' : response.xpath('//h1/text()').get(),
            'Annee' : response.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()').get(),#marche dans le shell voir video Scraping the top 250 movie ratings in IMDB (part 1) by Python
            'Score' : response.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()').get(),
            'Duree' : response.xpath('//li[@class="ipc-inline-list__item"]/text()').getall(),
            'Acteur' : response.xpath('//section[@class="ipc-page-section ipc-page-section--base sc-bfec09a1-0 bzDutS title-cast title-cast--movie  celwidget"]/div[@class="ipc-shoveler ipc-shoveler--base ipc-shoveler--page0 title-cast__grid"]/div[@class="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid"]/div[@class="sc-bfec09a1-5 dGCmsL"]/div[@class="sc-bfec09a1-7 iDmJtd"]/a[@class="sc-bfec09a1-1 gfeYgX"]/text()').getall(),
            'Genre' : response.xpath('//span[@class="ipc-chip__text"]/text()').getall(),
            'Description' : response.xpath('//span[@class="sc-16ede01-2 gXUyNh"]/text()').get(),
            'Public' : response.xpath('//a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"]/text()').getall()[1],
            'Pays' : response.xpath('//section[@class="ipc-page-section ipc-page-section--base celwidget"]/div[@class="sc-f65f65be-0 ktSkVi"]/ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base"]/li[@class="ipc-metadata-list__item"]/div[@class="ipc-metadata-list-item__content-container"]/ul[@class="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base"]/li[@class="ipc-inline-list__item"]/a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').get()
            
            }     

