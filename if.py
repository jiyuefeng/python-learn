#!/user/bin/env python3
# -*- coding:utf-8 -*-

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

## 这里返回的是字符串
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')    