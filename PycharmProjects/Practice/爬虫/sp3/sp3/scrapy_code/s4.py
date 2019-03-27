from twisted.web.client import getPage, defer
from twisted.internet import reactor

def all_done(arg):
    reactor.stop()


def onedone(response):
    print(response)


@defer.inlineCallbacks
def task():
    deferred2 = getPage(bytes("http://www.baidu.com", encoding='utf8'))
    deferred2.addCallback(onedone)
    yield deferred2

    stop_deferred = defer.Deferred()
    # stop_deferred.callback("sdfsdf")
    yield stop_deferred


ret = task()
ret.addBoth(all_done)

reactor.run()