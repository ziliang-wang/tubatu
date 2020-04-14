import json
import re
import scrapy
from tubatu_project.items import TubatuProjectItem


class TubatuSpider(scrapy.Spider):

    name = 'tubatu'
    url = 'https://xiaoguotu.to8to.com/tuce/p_1.html'

    def start_requests(self):
        yield scrapy.Request(self.url)

    def parse(self, response):
        # print(response.request.headers)
        item_list = response.xpath('//div[@class="item"]')[1:]
        id_search = re.compile(r'(\d+)\.html')
        for item in item_list:
            data_dict = {}
            data_dict['content_name'] = item.xpath('./div/a/@title').extract_first()
            data_dict['content_url'] = 'https:' + item.xpath('./div/a/@href').extract_first()
            data_dict['content_id'] = id_search.search(data_dict['content_url']).group(1)
            data_dict['request_url'] = 'https://xiaoguotu.to8to.com/case/' \
                  'list?a2=0&a12=&a11={}&a1=0'.format(data_dict['content_id'])

            yield scrapy.Request(data_dict['request_url'],
                                 callback=self.parse_detail,
                                 meta=data_dict)

        next_url = response.xpath('//a[@id="nextpageid"]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,
                                 callback=self.parse)

    def parse_detail(self, response):

        item = TubatuProjectItem()
        res = json.loads(response.text)
        for data in res['dataImg']:
            for info in data['album']:
                if info['l']['cid'] == int(response.meta['content_id']):
                    item['content_name'] = response.meta['content_name']
                    item['content_id'] = response.meta['content_id']
                    item['content_url'] = response.meta['content_url']
                    item['nick_name'] = info['l']['n']
                    item['pic_name'] = info['l']['t']
                    # item['pic_url'] = 'https://pic1.to8to.com/case/' + info['l']['s']
                    item['image_urls'] = ['https://pic1.to8to.com/case/' + info['l']['s']]
                    yield item



