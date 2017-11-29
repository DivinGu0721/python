# -*- coding:utf-8 -*-

number = 25
guess = int (raw_input("请输入你猜想的数字："))
if number == guess:
    print "你猜中啦"
elif number < guess:
    print "数字太大了"
else:
    print "数字太小了"

print "游戏结束了"







#修改版本，加入循环
guess = int(raw_input("请输入你猜想的数字："))
number = 25
while guess !=number:
    guess = int(raw_input("猜错了，请重新输入吧："))
    if number == guess:
        print "你猜中啦"
        print "游戏结束了"
    elif number < guess:
        print "数字太大了"
    else:
        print "数字太小了"


print "你猜中啦"
print "游戏结束了"