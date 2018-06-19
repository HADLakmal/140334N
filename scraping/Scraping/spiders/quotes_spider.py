import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # start_urls = [
    #     'http://www.todaytvseries2.com/tv-series'
    #
    # ]

    def start_requests(self):
        urls = [
                    'http://www.todaytvseries2.com/tv-series'
                ]
        for i in range (12, 330, 12):
            base_url = 'http://www.todaytvseries2.com/tv-series?start='
            new_url = base_url +str(i)
            urls.append(new_url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.uk-width-medium-1-1 article.uk-article '):
            yield {
                'title': quote.css('a::text').extract_first(),
                'episode': quote.css('p::text').extract_first(),
                'time': quote.css('p time::text').extract_first(),
                'description' : quote.css('div.teasershort p::text').extract_first(),
                'image_url': quote.css('div.uk-width-1-1 a::attr(href)').extract_first(),
                'rating': quote.css('div.size-1 span.extravote-info::text').extract_first(),
                'download': quote.css('p.uk-margin-top a.uk-buttonb::text').extract_first(),
                'link': quote.css('p.uk-margin-top a::attr(href)').extract_first(),

                'title&episode': quote.css('a::text').extract_first()+" "+quote.css('p::text').extract_first(),
                'title&rating': quote.css('a::text').extract_first() +" "+quote.css('div.size-1 span.extravote-info::text').extract_first(),
            }



