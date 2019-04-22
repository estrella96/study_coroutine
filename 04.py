import threading
import asyncio

#使用协程
@asyncio.coroutine
def hello():
    print('Hell world! (%s)' % threading.currentThread())
    print('Start..... (%s)' % threading.currentThread())
    yield from asyncio.sleep(10)
    print('Done.... (%s)' % threading.currentThread())
    print('Hell again! (%s)' % threading.currentThread())

#启动消息循环
loop=asyncio.get_event_loop()
#定义任务
tasks=[hello(),hello()]
#等待task执行完
loop.run_until_complete(asyncio.wait(tasks))
#关闭消息循环
loop.close()
