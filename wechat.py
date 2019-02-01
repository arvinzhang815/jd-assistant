#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import itchat
import time

itchat.auto_login(hotReload=True)
names = '张冰冰'
send_txt = u'祝{},新年快乐'

# while (True):
boom_remark_name = names
message = "test"
# boom_obj = itchat.search_friends(remarkName=boom_remark_name)
# itchat.send_msg(msg=message, toUserName=boom_obj)
boom_obj = itchat.get_friends()
# test = itchat.get_chatrooms()
# print(test)
# print(itchat.search_friends())
# print(itchat.search_friends(name='阿英'))
# print(itchat.search_friends(wechatAccount='蒲公英'))
# print(itchat.search_friends(userName='@9d8227110ba5b4b17ce203e622bd23644cb636bffebfc81d706bbf7f5935baf3'))
# itchat.send_msg()
# itchat.send("hello, file", toUserName='@9d8227110ba5b4b17ce203e622bd23644cb636bffebfc81d706bbf7f5935baf3')
# print("send success")
# time.sleep(10)
for friend in boom_obj:
    try:
        print(send_txt.format(friend['DisplayName'] or friend['NickName']) + "--userName:" + friend['UserName'] + "--remarkName:" + friend['RemarkName'] + "--friend['DisplayName']" +friend['DisplayName'] + "--friend['NickName']" + friend['NickName'])
    except Exception as a:
        print(a)
