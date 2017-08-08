#!/user/bin/env python3
# -*- coding:utf-8 -*-
list1 = ['a','b','c']
print(list1)
print(len(list1))
print(list1[0])
print('取最后一个元素',list1[-1])
list1.append('d')
print('list.append(\'d\') == ',list1[-1])
list1.insert(0, 'x')
print('list.insert(0, \'x\') == ',list1[0])

print(list1)
list1.pop()
print(list1)
print('list.pop() == ',list1[-1])

list1[0] = 'u'
print(list1)

list2 = []
print(list2)
print(len(list2))

t = ()
print(t)

t = (1,)
print(t)

t = (1,2)
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

for x in L:
	print(x)

y = list(range(10))
print(y)

L2 = ['Bart', 'Lisa', 'Adam']
for x in L2:
		print('hello, ', x)	

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)		