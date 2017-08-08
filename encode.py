#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ord 获得字符的整数， chr获得整数对应的字符
print(ord('A'))
print(chr(65))

print('ABC'.encode('ascii'))
print('中文'.encode('UTF-8'))
print('计算字符数',len('ABC'))
## 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print('计算字节数',len('这是一首简单的小情歌'.encode('UTF-8')))

print('hello, %s' % 'perrone')
print('hello, %s, you %s' % ('perrone','good'))

s1 = 72
s2 = 85

r = (s2 - s1)/ s1
print('%.2f' % r)