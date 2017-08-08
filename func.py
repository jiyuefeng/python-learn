#!/user/bin/env python3
# -*- coding:utf-8 -*-

print(bool(1))
print(bool(0))
print(bool(''))
print(bool())
print(int(0.1))
print(float(0.1))
print(str(0.1))

a = abs
## 别名
print(a(-22))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-22))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')               
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')            
enroll('Adam', 'M', age=9, city='Tianjin')            