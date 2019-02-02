#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import itchat
from tuling import getResponse


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return '冰恋丶：' + getResponse(msg["Text"])["text"]

itchat.auto_login(hotReload=True)
itchat.run()
