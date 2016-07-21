# -*- coding: utf-8 -*-

# ：）

print('——————————————————')
print('\n欢迎使用BMI健康指数计算程序')
print('■■')
print('■■■■')
print('■■■■■■■■')
print('■■■■■■■■■■■■')
print('■■■■■■■■■■■■■■■■')
print('■■■■■■■载入完成■■■■■■■')
print('——————————————————')

# Code

print('\n   ')
height = int(input('请输入你的身高(如175)：'))
weight = int(input('体重（如80）：'))
h = height/100
bmi = weight/(h*h)
if bmi < 18.5:
	print('\n您的指数为：%d 过轻。警告：地球对您的引力值即将降为零.' % bmi)
elif bmi <=25:
	print('\n您的指数为：%d 正常。That\'Perfact！' % bmi)
elif bmi <=28:
	print('\n您的指数为：%d 过重。及时关注体重，否则游泳不用圈。' % bmi)
elif bmi <=32:
	print('\n您的指数为：%d 肥胖。我处有99折健身卡售卖。' % bmi)
else:
	print('\n您的指数为：%d。需要注意身体健康了！' % bmi)
print('\n   ')
print('\n          欢迎再次使用 ^_^')
print('——————————————————')