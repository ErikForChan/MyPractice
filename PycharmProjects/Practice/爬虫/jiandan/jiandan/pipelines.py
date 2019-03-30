# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests


class JiandanPipeline(object):

    count = 1

    def process_item(self, item, spider):
        result = requests.get(item['img_url'])
        with open("D:/temp/jiandan/"+str(self.count)+".jpg",'wb') as f:
            f.write(result.content)
            f.close()
        self.count += 1
        return item
