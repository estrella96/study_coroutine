#直接使用生成器
L=[x*x for x in range(5)]#列表生成器
g=(x*x for x in range(5))#生成器
print(type(L))
print(type(g))

#函数 yield在函数中返回
def odd():
    print("11")
    yield 1
    print("22")
    yield 2
    print("33")
    yield 3
g=odd()
one=next(g)
print(one)

two=next(g)
print(two)

#for 循环
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n +=1
    return 'Done'
g=fib(5)
for i in g:
    print(i)