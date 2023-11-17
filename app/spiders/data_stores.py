import scrapy
from scrapy.http.response.html import HtmlResponse
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from app.models.store import Store, StoreSQL
# from app.database.persistence import create


class KabumSpider(scrapy.Spider):
    name = "kabum"
    start_urls = [
        "https://br.trustpilot.com/review/www.kabum.com.br",
        "https://br.trustpilot.com/review/mercadolibre.com.br",
    ]
    

    def parse(self, response: HtmlResponse):
        pre_url = response.css('.styles_prefix__a6Wee::text').get()
        pos_url = response.css('.styles_suffix__2BIZf::text').get()
        if not pre_url.startswith("www."):
            pre_url = "www."+pre_url
        store_url = "https://" + pre_url + pos_url
        store_name = response.xpath(
            "//*[@class='typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM']/text()"
        ).get()
        store_description = response.xpath(
            "//*[@class='styles_container__9nZxD customer-generated-content']/text()"
        ).get()
        store_rating = response.xpath(
            "//span[@class='typography_heading-m__T_L_X typography_appearance-default__AAY17']/text()"
        ).get()
        store_dict = {
            "store_name": store_name,
            "store_url": store_url,
            "store_description": store_description,
            "store_rating": store_rating,
        }
        # store = Store(**store_dict)
        # create(value=store, data_tuple=(StoreSQL, StoreSQL.store_id))
        yield scrapy.Request(store_url, callback=self.parse_category)

    def parse_category(self, response: HtmlResponse):
        if "kabum" in response.url:
            links = response.css(".sc-cdc9b13f-10 jaPdUR productLink").getall()
    
    def parse_items(self, response: HtmlResponse):
        links = response.css(".sc-cdc9b13f-10 jaPdUR productLink").getall() 


        
# def run_spider_programmatically():
#     process = CrawlerProcess(get_project_settings())
#     process.crawl(KabumSpider)
#     process.start()
