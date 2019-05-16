# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess


from spiders import GUI

search = list()
result1 = list()


class AmazonSpider(scrapy.Spider):
    name = 'snapdeal'
    allowed_domains = ['snapdeal.in']

    # search = input("enter your search:- ")
    # start_urls = ['https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+search]

    start_urls = search

    def parse(self, response):
        headers = response.xpath('//p[@class="product-title"]/text()').extract()
        prices = response.xpath('//span[@class= "lfloat product-price"]/text()').extract()

        print(headers)
        print(prices)

        print("showing results from AMAZON.IN ....,.,.,.,.,.,.,.,.,.,.,....")
        result1.append('<<<SHOWING RESULTS FROM SNAPDEAL>>>')
        for i in range(len(headers)):
            print(headers[i])
            print(prices[i])
            result1.append(headers[i] + " :- " + prices[i] + "\n")


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.in']

    # search = input("enter your search:- ")
    # start_urls = ['https://www.flipkart.com/search?q='+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']

    start_urls = search

    def parse(self, response):
        header = response.xpath('//div[@class="_3wU53n"]/text()').extract()
        price = response.xpath('//div[@class="_1vC4OE _2rQ-NK"]/text()').extract()

        header1 = response.xpath('//a[@class="_2cLu-l"]/text()').extract()
        price1 = response.xpath('//div[@class="_1vC4OE"]/text()').extract()


        print("Showing result from FLIPKART...............,.,.,.,.,")
        result1.append("<<<SHOWING RESULTS FROM FLIPKART>>>")
        if len(header) > 0:
            for i in range(len(header)):
                result1.append(header[i] + " :- " + price[i] + "\n")
                print(header[i])
                print(price[i])

        if len(header1) > 0:
            for i in range(len(header1)):
                result1.append(header1[i] + " :- " + price1[i] + "\n")
                print(header1[i])
                print(price1[i])


def amazon():
    GUI.GUI1()


def search1(topic):  # FOR AMAZON
    if (topic == None):
        return None

    else:
        search.append('https://www.snapdeal.com/search?keyword='+ topic +'&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy')
        search.append("https://www.flipkart.com/search?q=" + topic + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

    process = CrawlerProcess()
    process.crawl(AmazonSpider)
    process.crawl(FlipkartSpider)
    process.start()

    return result1


if __name__ == "__main__":
    amazon()
