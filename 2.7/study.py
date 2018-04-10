# -*- coding:utf-8 -*-
#使用r 加上引号 输出原始字符串 不对反斜杠进行转义

a = r"abbbb  \  \  aabcc"
print （a）
#三引号 输出多行字符串

b ="""啊啊啊
啊啊啊
啊啊啊
啊啊啊啊
啊啊啊啊啊啊4144141
发发发"""
print b

#三元操作符，下列两种方式等价
 x,y =4,5
if x<y:
 small=x
else:
 small=y

small=x if x<y else y
