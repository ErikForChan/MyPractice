from scrapy import signals
# 信号

class MyExtension(object):
    def __init__(self,value):
        self.value = value

    @classmethod
    def from_crawler(cls,crawler):
        val = crawler.settings.getint('')
        ext = cls(val)
        crawler.signals.connect(ext.open,signal = signals.spider_opened)
        crawler.signals.connect(ext.close,signal = signals.spider_closed)
        return ext

    def open(self):
        print("open")

    def close(self):
        print("close")


