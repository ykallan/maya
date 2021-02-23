import scrapy


class MayaSpider(scrapy.Spider):
    name = 'maya'
    allowed_domains = ['vmaya.com']
    start_urls = ['http://vmaya.com/']

    def parse(self, response):
        links = response.xpath('//dd/a[@class="cBlack1"]/@href').getall()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_lists)

    def parse_lists(self, response):
        links = response.xpath('//ul/li/h4/a/@href').getall()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath('//div[@class="spxq_qgjgk"]/div[1]/a/text()').get()
        describe = response.xpath('//div[@class="spxq_qgjgk"]/div[1]/a/text()').get()
        # price = response.xpath('//div[@class="spxq_qgjgk"]/div[@class="spxq_qgjg"][1]/div/b/text()').get()
        price = response.xpath('//div[contains(@class,"spxq_qgjgk")]/div[@class="spxq_qgjg"][1]/div/b/text()').get()
        phone = response.xpath('//div[@class="spxq_qgjgk"]/span[3]/div[2]/div[2]/text()').get()
        if not phone:
            phone = response.xpath('//div[@style="float:left; width:80px; height:18px; line-height:18px; color:#555555;"]/text()').get()


        item = {}
        item['title'] = title
        item['describe'] = describe
        item['price'] = price
        item['phone'] = phone
        item['url'] = response.url
        yield item

