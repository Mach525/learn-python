# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('苹果：',L[0][0])	
print('\n语言：',L[1][1])
print('\n谁？',L[2][2])

print(L[0][0])
print(L[len(L)-2][1])				# 用倒数实现！
print(L[len(L[2])-1][2])