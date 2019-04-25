import re
p=re.compile(r'\d+')
#3-6查找范围 只找一个
m=p.match("one234sdfzcbshdqw9745dfnjdfh23",3,6)
print(m)

m=p.search("one234sdfzcbshdqw9745dfnjdfh23")
print(m.group())
#I 忽略大小写
p=re.compile(r'([a-z]+) ([a-z]+)',re.I)

m=p.match("I am dfe asdfdas")
print(m)