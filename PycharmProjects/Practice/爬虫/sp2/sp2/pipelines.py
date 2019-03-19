# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipeline是全局的，所有爬虫都会执行


class Sp2Pipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):

        # item 爬虫中yield回来的对象
        print(item)
        # spider 爬虫对象
        if spider.name == 'jiadnan':
            self.f.write(item)
        # print(item)
        return item
        # from scrapy.exceptions import  DropItem
        # raise  DropItem() # 下一个pipeline的process_item不会执行
    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.get('MMMM')
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.f = open('jiandan.log','a+')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('关闭爬虫')
        self.f.close()

"""
检测 CustomPipeline类中是否有 from_crawler方法
如果有：
       obj = 类.from_crawler()
如果没有：
       obj = 类()
obj.open_spider()

while True:
    爬虫运行，并且执行parse各种各样的翻缸发，yield item
    obj.process_item()

obj.close_spider()    

"""