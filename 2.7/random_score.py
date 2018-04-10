# -*- coding:utf-8 -*-

#随机生成考试成绩，变按照成绩分档



import random
score = random.randint(1,100)
if 80< score<=100:
    print 'A'
elif 60< score <=80:
    print 'B'
elif 40<score <= 60:
    print 'C'
else:
    print 'laji'