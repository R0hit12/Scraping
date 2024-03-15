import scrapy
import pandas as pd
import unicodedata


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    start_urls = [
        "https://www.amazon.in/s?k=shoes+for+men&crid=JAVU9OVPE4Y9&sprefix=shoes+for+men%2Caps%2C289&ref=nb_sb_ss_ts-doa-p_1_13"
    ]

    def __init__(self):
        self.page_count = 0  # Initialize page count
        self.watch_data = []

    # def start_requests(self):
    #     yield scrapy.Request(url="https://www.amazon.in/s?k=shoes+for+men&crid=JAVU9OVPE4Y9&sprefix=shoes+for+men%2Caps%2C289&ref=nb_sb_ss_ts-doa-p_1_13",
    #                          callback=self.parse,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})

    def parse(self, response):
        self.page_count += 1

        products = response.xpath("//div[@data-component-type='s-search-result']")

        for product in products:
            brand = product.xpath(".//div/h2/span/text()").get()
            price = product.xpath(".//span[@class='a-price-whole']/text()").get()
            discount = product.xpath(".//span[contains(text(), 'off')]/text()").get()
            link = product.xpath(".//a[@class='a-link-normal s-no-outline']/@href").get()
            absolute_link = "https://www.amazon.in/"+link

            self.watch_data.append({
                "Brand": brand.strip() if brand else None,
                "Price": price.strip() if price else None,
                "Discount": discount.strip() if discount else None,
            })

            yield {
                "link":absolute_link,
            }
            yield response.follow(absolute_link)




            # next_page_url = response.xpath("//div/div/span/a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']/@href").get()
            # if next_page_url and self.page_count <3:
            #     yield response.follow(next_page_url, callback=self.parse)





    # def closed(self, reason):
    #     print("Spider closed. Reason:", reason)
    #     df = pd.DataFrame(self.watch_data)
    #     print(df)
    #     try:
    #         df.to_excel("scrapy_amazon.xlsx")
    #         print("Excel file written successfully.")
    #     except Exception as e:
    #         print("Error writing Excel file:", e)
