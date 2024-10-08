from scrapy import Spider, Request

'''
    1- //a[contains(@class, "navlabellink nvoffset")]
    2- //div[@class='nchildren']//a[contains(@class, "navlabellink nvoffset nnormal")]  OR  //div[@class='nchildren']//tr/td[3]/a
    3- //div[contains(@class, 'ranavnode')]//div[contains(@class,'ranavnode')]//div[contains(@class,'ranavnode')]//a[2]
    REALIZED SOMETHING...
        Every node has a class of 'ranavnode', so this kind of shit works... ↓↓↓
            //div[contains(@class, 'ranavnode')]//div[contains(@class,'ranavnode')]//div[contains(@class,'ranavnode')]
        
        sooo... I could run spiders through every node, appending //div[contains(@class, 'ranavnode')] again and again until leaf node...
    LET'S TRY IT:
        1- //div[contains(@class,'ranavnode')] ←← gets some hidden inputs(wrong) OR //div[contains(@class,'ranavnode')]/input[contains(@value,'"make"')] ←← gets normal inputs(right)
        2- 
    
'''
'''
    To get the name of parts: //div[@class="listing-text-row-moreinfo-truck"]
    To get the prices of parts: //td[contains(@id,"listingtd")]/span/span/span/text()
'''


class SpRockautoSpider(Spider):
    name = "sp_rockauto"
    # allowed_domains = ["www.rockauto.com"]
    start_urls = ["https://www.rockauto.com"]

    def parse(self, response):
        models = response.xpath('//div[@class="ranavnode"]//td[@class="nlabel"]/a')
        # for model in models:
        #     yield {
        #         "link": model.xpath("@href").get(),
        #         "txt": model.xpath("text()").get(),
        #         "id": model.xpath("@id").get(),
        #     }
        
        
        # counter += 1
        # yield Request(f'https://www.rockauto.com{models[counter].xpath("@href").get()}', self.parse)
        
        yield Request(f'https://www.rockauto.com/en/catalog/acura,2024,integra,1.5l+l4+turbocharged,3454229,belt+drive,belt,8900', self.parse)
        
        
        items = response.xpath('//tbody[contains(@id, "listingcontainer")]/tr[1]')
        print(len(items))
        for item in items:
            yield {
                "part_manufacturer": item.xpath('//div[@class="listing-text-row-moreinfo-truck"]/span[1]/text()').get(),
                "part_number": item.xpath('//div[@class="listing-text-row-moreinfo-truck"]/span[2]/text()').get(),
                "info_link": item.xpath('//div[@class="listing-text-row-moreinfo-truck"]/a/@href').get(),
                "price": item.xpath('//td[contains(@id,"listingtd")]/span/span/span[contains(@id, "dprice")]/text()').get(),
            }


        # yield Request(f'https://www.rockauto.com/en/catalog/acura', self.parse)
        # yield Request(f'https://www.rockauto.com/en/catalog/ac', self.parse)