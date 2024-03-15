import scrapy


class DetailsSpider(scrapy.Spider):
    name = "details"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/Lancer-White-Sports-Running-Indus-251/product-reviews/B081LGBPT7/ie=UTF8&reviewerType=all_reviews&pageNumber=2"]
    # custom_settings = {
    #     'ROBOTSTXT_OBEY': False
    # }


    def __init__(self):
        self.page_count = 0
    def parse(self, response):

        # self.page_count+=1
        next_page_url = response.css('#cm_cr-pagination_bar > ul > li.a-last > a::attr(href)').get()
        yield {
            "link-----------":next_page_url
        }
        review_element = response.xpath("//*[@class='a-section celwidget']")

        for i in review_element:
            stars = i.xpath(".//div/a/i/span/text()").get()
            customer = i.xpath(".//span[@class='a-profile-name']/text()").get()
            review = i.xpath(".//span[@data-hook='review-body']/span/text()").get()
            date = i.xpath(".//span[@data-hook='review-date']/text()").get()

            yield {
                "Rating": stars if stars else None,
                "Customer": customer if customer else None,
                "Review": review if review else None,
                "Date": date if date else None
            }
        next_page_link = "https://www.amazon.in"+str(next_page_url)
        yield {
            "urll====-----=-=====":next_page_link

        }
        new_url = response.urljoin(next_page_link)
        print(new_url)
        yield scrapy.Request(url=new_url,callback=self.parse)


        # self.page_count+=1
        # new_url = "https://www.amazon.in/Lancer-White-Sports-Running-Indus-251/product-reviews/B081LGBPT7/ie=UTF8&reviewerType=all_reviews&pageNumber={0}".format(self.page_count)
        # if new_url and self.page_count <4:
        #     yield response.follow(next_page_link,callback=self.parse)









