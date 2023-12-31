import scrapy
from scrapy.http.response.html import HtmlResponse

from app.services.decorators import run_once
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from app.models.store import Store, StoreSQL
from app.models.product import Product, ProductSQL
from app.database.persistence import create


class StoreSpider(scrapy.Spider):
    tuple_product = (ProductSQL, ProductSQL.product_id)
    tuple_store = (StoreSQL, StoreSQL.store_id)
    name = "stores"

    start_urls = [
        "https://br.trustpilot.com/review/magazineluiza.com.br",
        "https://br.trustpilot.com/review/havan.com.br"
    ]

    def parse(self, response: HtmlResponse):
        pre_url = response.css(".styles_prefix__a6Wee::text").get()
        pos_url = response.css(".styles_suffix__2BIZf::text").get()
        if not pre_url.startswith("www."):
            pre_url = "www." + pre_url
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
        if not store_rating:
            store_rating = "0"
        store_dict = {
            "store_name": str(store_name),
            "store_url": str(store_url),
            "store_description": str(store_description),
            "store_rating": str(store_rating),
        }
        store = Store(**store_dict)
        create(value=store, data_tuple=self.tuple_store)
        yield scrapy.Request(store_url, callback=self.parse_category)

    def parse_category(self, response: HtmlResponse):
        if "magazine" in response.url:
            links = response.xpath('//ul[@class="sc-cPyLVi hnUCVe"]//a/@href').getall()
            for link in links:
                yield scrapy.Request(
                    link,
                    callback=self.parse_products,
                )
        if "havan" in response.url:
            links = response.xpath(
                '//ul[contains(@class, "menu__inner-list menu__inner-list")]/li/a/@href'
            ).getall()
            for link in links:
                if not link == "#":
                    yield scrapy.Request(
                        link,
                        callback=self.parse_products,
                    )

    def parse_products(self, response: HtmlResponse):
        if "magazine" in response.url:
            links = response.xpath('//li[@class="sc-APcvf eJDyHN"]//a/@href').getall()
            for link in links:
                yield scrapy.Request(
                    response.urljoin(link),
                    callback=self.parse_product,
                )
            pagination = response.xpath(
                '//ul[@class="sc-isRoRg fPwgEt"]//a/@href'
            ).get()
            if pagination:
                yield scrapy.Request(
                    response.urljoin(pagination), callback=self.parse_products
                )
        if "havan" in response.url:
            links = response.xpath(
                '//li[contains(@class, "item product product-item")]//a/@href'
            ).getall()
            for link in links:
                if not link == "#":
                    yield scrapy.Request(
                        link,
                        callback=self.parse_product,
                    )
            pagination = response.xpath(
                '//ul[@class="items pages-items"]//a/@href'
            ).get()
            if pagination:
                yield scrapy.Request(pagination, callback=self.parse_products)

    def parse_product(self, response: HtmlResponse):
        if "magazine" in response.url:
            product_name = response.xpath("//h1/text()").get()
            description = response.xpath(
                '//div[@class="sc-fqkvVR hlqElk sc-jcdlHQ cxsdMT"]/text()|//div[@class="sc-fqkvVR hlqElk sc-jcdlHQ cxsdMT"]/p/text()'
            ).get()
            if description:
                description = description[0:100]
            category = response.xpath(
                '(//a[@class="sc-koXPp bXTNdB"])[2]//text()'
            ).get()
            brand = response.xpath(
                '//td[text()="Marca"]/following-sibling::td//text()'
            ).get()
            model = response.xpath(
                '//td[text()="Modelo"]/following-sibling::td//text()'
            ).get()
            price = str(
                response.xpath('//div[@class="sc-dcJsrY bCfntu"]//p/text()').get()
            ).replace("\xa0", "")
            price = price.replace("R$", "")
            average_rating = str(
                response.xpath("//span[@class='sc-kpDqfm jYhqpO']//text()").get()
            )
            if average_rating == "None":
                average_rating = "0"
            availability = response.xpath(
                "//div[@class='sc-dhKdcB kbCiGN']//label/text()"
            ).get()
            availability = True if availability else False
            image_url = response.xpath("//img[@class='sc-cWSHoV jnuWYf']/@src").get()
            product = {
                "product_name": str(product_name),
                "description": str(description),
                "category": str(category),
                "brand": str(brand),
                "model": str(model),
                "price": str(price),
                "product_url": response.url,
                "average_rating": str(average_rating),
                "availability": str(availability),
                "image_url": str(image_url),
                "store_id": 1,
            }
            product = Product(**product)
            create(value=product, data_tuple=self.tuple_product)
            yield product
        if "havan" in response.url:
            product_name = response.xpath("//h1/span/text()").get()
            description = response.xpath(
                "//div[@class='product attribute description']//p/text()"
            ).get()
            if description:
                description = description[0:100]
            category = None
            brand = response.xpath(
                "//td[text()='Marca']/following-sibling::td//text()"
            ).get()
            model = response.xpath(
                "//div[@class='product attribute description']//p//text()[contains(., 'Modelo:')]"
            ).get()
            if model:
                model = model.replace("\r\nModelo:", "").replace("\u00a0", "")
            price = response.xpath("//span[@class='price']/text()").get()
            price = price.replace("R$\xa0", "")
            average_rating = None
            availability = response.xpath(
                "//button[@id='product-addtocart-button']//p[text()='Comprar']/text()"
            ).get()
            availability = True if availability else False
            image_url = response.xpath("//div[@class='product media']//img/@data-src").get()
            
            product = {
                "product_name": str(product_name),
                "description": str(description),
                "category": str(category),
                "brand": str(brand),
                "model": str(model),
                "price": str(price),
                "product_url": response.url,
                "average_rating": str(average_rating),
                "availability": str(availability),
                "image_url": str(image_url),
                "store_id": 2,
            }
            product = Product(**product)
            create(value=product, data_tuple=self.tuple_product)
            yield product


@run_once
def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(StoreSpider)
    process.start()
