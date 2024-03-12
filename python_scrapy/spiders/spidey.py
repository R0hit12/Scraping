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

    def parse(self, response):
        # Increment page count
        self.page_count += 1

        # Extract book titles and links from the current page
        for i in response.xpath("//article/h3/a"):
            title = i.xpath(".//text()").get()
            link = i.xpath(".//@href").get()
            self.book_title.append(title)

            yield {
                "Book name": title,
                "Book link": link
            }

        print(self.book_title)
        print("length================", len(self.book_title))

        # Extract URL of the next page
        next_page_url = response.xpath("//li[@class='next']/a/@href").get()

        # If there's a next page and the page count is less than 5, follow the link
        if next_page_url and self.page_count < 5:
            yield response.follow(next_page_url, callback=self.parse)