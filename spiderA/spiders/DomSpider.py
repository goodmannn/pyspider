from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


class DomzSpider(CrawlSpider):
    name = "domz"
    allowed_domains = ["list.jd.com"]
    start_urls = ["https://list.jd.com/list.html?cat=670,671,1105&page=2&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"]

    rules = [
        Rule(SgmlLinkExtractor(allow='&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main', restrict_xpaths='//a[@class="pn-next"]'),
             callback='parse_item', follow=True)
    ]

    def parse(self, response):
        sel = Selector(response)
        blog_url = str(response.url)
        blog_name = sel.xpath('//div[@id="asideHotArticle"]/div/ul/li/a/text()').extract()
        for x in blog_name:
            print x
