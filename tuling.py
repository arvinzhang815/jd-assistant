#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests


def getResponse(info):
    api_url = 'http://www.tuling123.com/openapi/api'

    data = {'key': '106115a28bda40b6b3690eaa832bd3bb', 'info': info, 'userid': 'wechat-reboot'}

    r = requests.post(api_url, data=data).json()

    return r