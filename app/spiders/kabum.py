import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from app.models.store import Store, StoreSQL
from app.database.persistence import create


def called_only_once(func):
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        else:
            return False

    wrapper.called = False
    return wrapper


class KabumSpider(scrapy.Spider):
    name = "kabum"
    start_urls = ["https://br.trustpilot.com/review/www.kabum.com.br"]

    @called_only_once
    def parse(self, response: HtmlResponse):
        kabum_store = {
            "store_name": response.xpath("//*[@class='typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM']/text()").get(),
            "store_url": response.xpath("//span[@class='styles_prefix__a6Wee']/text()").get()
            + response.xpath("//span[@class='styles_suffix__2BIZf']/text()").get(),
            "store_description": response.xpath("//*[@class='styles_container__9nZxD customer-generated-content']/text()").get(),
            "store_rating": response.xpath("//span[@class='typography_heading-m__T_L_X typography_appearance-default__AAY17']/text()").get(),
        }

        from app.database.persistence import create
        from app.models.store import Store, StoreSQL
        ddd = (StoreSQL,StoreSQL.store_id)
        a = Store(**kabum_store)
        create(value=a, data_tuple=ddd)
        yield kabum_store
        


def run_spider_programmatically():
    process = CrawlerProcess(get_project_settings())
    process.crawl(KabumSpider)
    process.start()

