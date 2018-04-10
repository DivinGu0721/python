# -*- coding:utf-8 -*-
from lxml import html
from lxml import etree
import requests

page = requests.get("http://society.qq.com/")
tree = html.fromstring(page.text)

names = tree.xpath("//a[@class='linkto']/text()")
names2 = tree.xpath("//a[@rel='nofollow']/text()")
#prices = tree.xpath("//span[@class='item-price']/text()")

print(names)
print(names2)

