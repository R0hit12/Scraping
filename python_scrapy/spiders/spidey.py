import scrapy

book_title = []
book_price = []
class SpideySpider(scrapy.Spider):
    name = "spidey"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def __init__(self):
        self.book_title = []
        self.page_count = 0  # Initialize page count
        self.book_price = []

    def details(self,response):
        description = response.xpath("//article/p/text()").get()
        availability = response.xpath("//tbody/tr[6]/td/text()").get()
        yield {
            "Description": description,
            "Availability": availability
        }

    def parse(self, response):
        # Increment page count
        self.page_count += 1

        # Extract book titles and links from the current page
        for i in response.xpath("//article"):
            title = i.xpath(".//h3/a/text()").get()
            link = i.xpath(".//h3/a/@href").get()
            price = i.xpath(".//div/p[@class='price_color']/text()").get()
            self.book_title.append(title)
            self.book_price.append(price)

            yield {
                "Book name": title,
                "Book_price": price,
                "Book_link": link,
            }

            product_link = response.xpath("")



        # Extract URL of the next page
        next_page_url = response.xpath("//li[@class='next']/a/@href").get()

        if next_page_url and self.page_count<3:


            yield response.follow(next_page_url, callback=self.parse)
            print("length================", len(self.book_title))
            print("length===================="
                  "====================", len(self.book_price))