#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import os
import random
import re
import matplotlib.pyplot as plt

import itchat
import PIL.Image as Image
from wordcloud import WordCloud


def get_head_imag():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)
    for count, friend in enumerate(friends):
        img = itchat.get_head_img(userName=friend['UserName'])
        imgFile = open('img/' + str(count) + '.jpg', 'wb')
        imgFile.write(img)
        imgFile.close()
    itchat.logout()


def get_signature():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)
    file = open('signature.txt', 'a', encoding='utf-8')
    for count, friend in enumerate(friends):
        signature = friend["Signature"].strip().replace('emoji', '').replace('span', "").replace('class', "")
        rec = re.compile('1f\d+\w*|[<>/=]')
        signature = rec.sub("", signature)
        file.write(signature + "\n")
    file.close()

    sex = dict()
    for f in friends:
        if f["Sex"] == 1:  # 男
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2:  # 女
            sex["women"] = sex.get("women", 0) + 1
        else:  # 未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 柱状图展示
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.savefig("getsex.png")  # 保存图片
    plt.ion()
    plt.pause(5)
    plt.close()  # 图片显示5s，之后关闭

def creat_cloud(file_name):
    text = open('{}.txt'.format(file_name), encoding='utf-8').read()

    # 设置词云
    wc = WordCloud(# 设置背景颜色
        background_color="white", # 设置最大显示的词云数
        max_words=2000, # 这种字体都在电脑字体中，window在C:\Windows\Fonts\下，mac下可选/System/Library/Fonts/PingFang.ttc 字体
        font_path='C:\\Windows\\Fonts\\simfang.ttf', height=500, width=500, # 设置字体最大值
        max_font_size=60, # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30, )

    myword = wc.generate(text)  # 生成词云 如果用结巴分词的话，使用wl 取代 text， 生成词云图
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('signature.png')  # 把词云保存下


def getSex():
    itchat.login()
    friends = itchat.get_friends(update=True)
    sex = dict()
    for f in friends:
        if f["Sex"] == 1:  # 男
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2:  # 女
            sex["women"] = sex.get("women", 0) + 1
        else:  # 未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 柱状图展示
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.savefig("getsex.png")  # 保存图片
    plt.ion()
    plt.pause(5)
    plt.close()  # 图片显示5s，之后关闭


def creat_img():
    x = 0
    y = 0
    imgs = os.listdir('img')
    random.shuffle(imgs)
    newImg = Image.new('RGBA', (640, 640))
    width = int(math.sqrt(640 * 640 / len(imgs)))

    numLine = int(640 / width)

    for i in imgs:
        try:
            img = Image.open("img/" + i)
            img = img.resize((width, width), Image.ANTIALIAS)
            newImg.paste(img, (x * width, y * width))
            x += 1
            if x >= numLine:
                x = 0
                y += 1
        except:
            pass

    newImg.save("all_all.png")


# get_head_imag()
# creat_img()
get_signature()
creat_cloud('signature')
