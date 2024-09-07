import scrapy

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



class SpRockautoSpider(scrapy.Spider):
    name = "sp_rockauto"
    # allowed_domains = ["www.rockauto.com"]
    start_urls = ["https://www.rockauto.com"]

    def parse(self, response):
        pass
