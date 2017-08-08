#!/user/bin/env python3
# -*- coding:utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
	print(key)

for value in d.values() :
	print(value)

for k, v in d.items() :
	print(k,' == ', v)

y = [k + ' ==== ' + str(v) for k, v in d.items()]

print(y)


from collections import Iterable
print(isinstance('abc',Iterable))

print(isinstance(d,Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

## 很厉害
r = [x * x for x in range(1,11) if x % 2 == 0]	
print(r)

import os
d = [d for d in os.listdir('.')]
print(d)


print('输出生成器')
q = (x * x for x in range(10))
for n in q:
	print(n)