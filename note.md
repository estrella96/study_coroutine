# 协程
## 迭代器
- 可迭代 Iterable:直接作用于for循环的变量
- 迭代器 Itertor:不但可以作用于for循环 还可以被next调用
- list可迭代但不是迭代器
- range是迭代器
- isinstance(变量,Iterable) isinstance(变量,Iterator)
- 转换iter(变量)
## 生成器 01.py
- generator 一边循环一边计算下一个元素的机制/算法
- 三个条件
    - 每次调用都产生for循环需要下一个的元素
    - 如果到最后一个 抛出StopIteration异常
    - 可以被next()函数调用
- 制作生成器
    - 直接使用
    - 函数 yield在函数中返回 用next()调用
    - for循环调用生成器 最典型的是range
## 协程
- 定义：允许不同入口点在不同位置按暂停或开始执行程序 一步步执行
- 可以暂停执行的函数 或者看作生成器
- 实现 02.py
    - yield返回
    - send调用
- 四个状态
    - inspect.getgeneratorstate()
    - GEN_CREATED 等待开始执行
    - GEN_RUNNING 解释器正在执行
    - GEN_SUSPENED 在yield处暂停
    - GEN_CLOSED 执行结束
    - next 预激
- 协程终止
- yield from 03.py
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止发出StopIteration异常 异常对象的value属性保存返回值
    - yield from从内部捕获StopIteration异常
    - 委派生成器
        - 包含yield from的生成器函数
        - 委派生成器在yield from处暂停，调用方可以直接把数据发给子生成器
        - 子生成器把产出的值发给调用方
        - 子生成器在最后 解释器抛出StopIteration异常，返回值附加到异常对象上
## asyncio
- 本身是一个消息循环
- 步骤
    - 创建消息循环
    - 把协程导入
    - 关闭
## async and wait
- 为了更好表示异步IO
- 让协程代码更简洁
- 用async替换@asyncio.coroutine
  await替换 yield from
## aiohttp
- asyncio 实现单线程的并发io 在客户端用处不大
- 在服务器端用asyncio+coroutine，因为http是io操作
- asyncio 实现了tco,udp,ssl等协议
- aiohttp是对asyncio实现的http框架
- pip install aiohttp安装
## concurrent.futures
- 类似其他语言的线程池的概念
- 利用multiprocessing 实现真正的并行计算（多核cpu）
- 核心原理：以子进程的形式 并行运行多个python解释器
每个子进程完整使用一个cpu内核
    - concurrent.futures.Executor
    - ThreadPoolExecutor
    - ProcessPoolExecutor
    - 执行时自行选择
    - submit(fn,args,kwargs) fn 异步执行的函数 args，kwargs参数
## Future
- 

        
    

