import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    start_urls = [
        "https://www.amazon.in/s?k=shoes+for+men&crid=JAVU9OVPE4Y9&sprefix=shoes+for+men%2Caps%2C289&ref=nb_sb_ss_ts-doa-p_1_13"]

    def parse(self, response):
        products = response.xpath("//div[@data-component-type='s-search-result']")

        for product in products:
            brand = product.xpath(".//div/h2/span/text()").get()
            price = product.xpath(".//span[@class='a-price-whole']/text()").get()
            discount = product.xpath(".//span[contains(text(), 'off')]/text()").get()

            yield {
                "Brand": brand.strip() if brand else None,
                "Price": price.strip() if price else None,
                "Discount": discount.strip() if discount else None,
            }
