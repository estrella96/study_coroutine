def simple_coroutine():
    print('start..')
    x=yield
    print('received',x)
sc=simple_coroutine()
print(1111)
#sc.send(None)
next(sc) #预激
print(2222)
sc.send('jack')