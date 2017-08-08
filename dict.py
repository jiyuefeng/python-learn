#!/user/bin/env python3
# -*- coding:utf-8 -*-


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

## 不存在的key 会报错

#print(d['lisa'])
print(d.get('lisa', -1))
print(d.get('lisa'))

print(d['Michael'])
d.pop('Michael')
print(d)

a = set([1, 2, 3,1])

print(a)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print('交集 ', s1 & s2)
print('并集 ', s1 | s2)