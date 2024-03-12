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

        print(self.book_title)
        print("length================", len(self.book_title))
        print("length========================================",len(book_price))

        # Extract URL of the next page
        next_page_url = response.xpath("//li[@class='next']/a/@href").get()

        # If there's a next page and the page count is less than 5, follow the link
        if next_page_url and self.page_count < 3:
            yield response.follow(next_page_url, callback=self.parse)
        print("length================", len(self.book_title))
        print("length========================================", len(book_price))