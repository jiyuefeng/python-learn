#!/user/bin/env python3
# -*- coding:utf-8 -*-

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d=100, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1,2)    
kw = {'d': 99, 'x': '#'}

## 传入可变参数 以及关键字参数
#f1(*args, **kw)
f2(*args, **kw)