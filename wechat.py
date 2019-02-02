#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import itchat
import time

itchat.auto_login(hotReload=True)
names = '张冰冰'
send_txt = u'测试轰炸器啊'

# while (True):
boom_remark_name = names
message = "test"
# boom_obj = itchat.search_friends(remarkName=boom_remark_name)
# itchat.send_msg(msg=message, toUserName=boom_obj)
# boom_obj = itchat.get_friends()
boom_obj1 = itchat.search_friends(name='阿英')
# boom_obj2 = itchat.search_friends(nickName ='周亚杰')
# print(boom_obj2)
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
# for friend in boom_obj:
#     try:
#         print(send_txt.format(friend['DisplayName'] or friend['NickName']) + "--userName:" + friend['UserName'] + "--remarkName:" + friend['RemarkName'] + "--friend['DisplayName']" +friend['DisplayName'] + "--friend['NickName']" + friend['NickName'])
#     except Exception as a:
#         print(a)
# flag = 1
# while True:
#     print(boom_obj1[0]['UserName'])
#     itchat.send_msg(send_txt, toUserName=boom_obj1[0]['UserName'])
#     print("success" + flag)
#     time.sleep(2)
#     flag = flag + 1
#     if flag > 10:
#         break
# itchat.logout()

#群聊
# itchat.auto_login(True)
#
# REAL_SINCERE_WISH = u'祝%s新年快乐！！'
#
# chatroomName = 'wishgroup'
# itchat.get_chatrooms(update=True)
# chatrooms = itchat.search_chatrooms(name=chatroomName)
# if chatrooms is None:
#     print(u'没有找到群聊：' + chatroomName)
# else:
#     chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
#     for friend in chatroom['MemberList']:
#         friend = itchat.search_friends(userName=friend['UserName'])
#         # 如果是演示目的，把下面的方法改为print即可
#         itchat.send(REAL_SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
#         time.sleep(.5)

#校验好友是否删除你
chatroomUserName = '@1234567'
friend = itchat.get_friends()[1]

r = itchat.add_member_into_chatroom(chatroomUserName, [friend])
if r['BaseResponse']['ErrMsg'] == '':
    status = r['MemberList'][0]['MemberStatus']
    itchat.delete_member_from_chatroom(chatroomUserName, [friend])
    # return {3: u'该好友已经将你加入黑名单。', 4: u'该好友已经将你删除。', }.get(status, u'该好友仍旧与你是好友关系。')