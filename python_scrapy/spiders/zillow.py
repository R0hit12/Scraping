import scrapy
from scrapy import Request
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

class MyRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return response

class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["www.zillow.com"]
    # start_urls = ["https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-96.94121531640624%2C%22east%22%3A-96.51824168359374%2C%22south%22%3A36.98512763437968%2C%22north%22%3A37.257783219071236%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"]

    custom_settings = {
        'RETRY_HTTP_CODES': [403],
        'RETRY_TIMES': 3,
    }

    def start_requests(self):
        url = 'https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-96.94121531640624%2C%22east%22%3A-96.51824168359374%2C%22south%22%3A36.98512763437968%2C%22north%22%3A37.257783219071236%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        # Your parsing logic here
        pass
    # def parse(self, response):
    #     pass
