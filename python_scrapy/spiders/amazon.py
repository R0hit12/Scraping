import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    start_urls = [
        "https://www.amazon.in/s?k=shoes+for+men&crid=JAVU9OVPE4Y9&sprefix=shoes+for+men%2Caps%2C289&ref=nb_sb_ss_ts-doa-p_1_13"]




    def __init__(self):
        self.page_count = 0  # Initialize page count

    def parse(self, response):
        self.page_count += 1

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

            next_page_url = response.xpath("//div/div/span/a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']/@href").get()
            if next_page_url and self.page_count < 4:
                yield response.follow(next_page_url, callback=self.parse)
