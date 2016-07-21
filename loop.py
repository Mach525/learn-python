# -*- coding: utf-8 -*-

# 将list或tuple变量loops带入loop变量中

loops = ['233','555','999','666']
for loop in loops:
	print('\n打印list或tuple',loop)

# 计算和 用sum变量做累加

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('\nsum做累加',sum)

# 生成range函数生成整数序列

sum = 0
for n in range(5001):
	sum = sum + n
print('\nrange函数',sum)

# 
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 利用循环依次对list中的名字输出hello world

L = ['Bart', 'Lisa', 'Adam']
n = 0
while n < len(L):
	print('Hello，%s' % L[n])
	n=n+1