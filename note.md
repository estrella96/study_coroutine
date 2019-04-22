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

# 结构化文件存储
- xml json
## XML
- XML extensibleMarkupLanguage
    - 标记语言 语言中使用<>的文本字符串标记
    - 可扩展：用户自定义需要的标记
    - 描述数据本身 数据的结构和语义
    - HTML侧重于如何显示web页面的数据
- XML 文档的构成 05.xml
    - 处理指令 第一行
        - 与XML本身处理相关的一些声明或代码
        - 版本 编码
    - 根元素 有且只有一个
    - 子元素
    - 属性
    - 内容 标签存储的信息
    - 注释 说明 标签里面没有注释 <!--     -->
- 保留字符的处理
    - 实体引用（转义）
        & &amp;
        < &lt;
        > &gt;
        ' &apos;
        " &quot; 
    - 把含保留字符的部分放入CDATA块内部 
        <![CDATA[代码块]]>
    
- 命名规则
    - Pascal命名法
    - 第一个字母大写
    - 大小写严格区分
    - 配对的标签一致
- 命名空间
    - 防止命名冲突 重复有相同元素的内容
    - xmlns 放在属性的位置
        xmls:名称="统一资源定位"
## XML访问
### 读取
- SAX 和 DOM
- SAX Simple API for XML
    - 基于事件驱动
    - 解析器和事件处理
    - 特点
        - 块
        - 流式读取
- DOM
    - XML编程接口
    - XML在缓存中以属性结构保存，读取
    - 用途
        - 定位和浏览XML任何一个节点信息
        - 添加删除相应内容
    - minidom
    - etree
### 写入 06.py
- 更改
    - ele.set
    - ele.append
    - ele.remove
- 生成创建
    - SubElement
    - minidom 写入
    - etree写入
## JSON JavaScriptObjectNotation
- 轻量级的数据交换格式 基于ECMAScript
- 键值对形式的数据集
    - key ：字符串
    - value：字符串 数字 列表 json
    - json用大括号包裹
    - 键值对用逗号隔开
    student={
        "name":"jasa",
        "age":18}
- json和python格式转换
    - 字符串 字符串
    - 数字 数字
    - 队列 list
    - 对象 dict
    - 布尔值 布尔值
- python for json 
    - json包
    - 转换 07.py
        - json.dumps():编码 python-->json
        - json.loads():解码 json-->python
    - python读取json文件
        - json.dump():内容写入文件
        - json.load():json文件内容读入python

# 正则表达式 RegularExpression,re
- 用于使用单子字符串来描述，匹配符合某个规则的字符串
- 用来检索替换某些模式的文本
- 
    
    
        
    

