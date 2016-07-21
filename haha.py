#！/usr/bin/env python3
# -*- coding: utf-8 -*-
t1 = int(input('请输入您的去年成绩：'))
l1 = int(input('请输入您的成绩：'))
c = (l1-t1)/l1*100
print('\n您去年的成绩为：%d分' % l1)
print('今年成绩为：%d分' % t1)
if l1>t1:
	print('\n恭喜相较去年上升了 %d%% 哦！' % c)
else:
	if t1==l1:
		print('\n您的成绩与去年相同哦，加油努力！')
	else:
		if t1>l1:
			print('\n您的成绩相较去年下降了 %d%% ' % c)