#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
import sys

import requests
import os


def load_picture_by_url(url, path, name):
    # headers = {'Authorization': 'Basic 7dfdc0e2440c06fa17dadf82ba6121'}
    # , headers = headers
    result = requests.get(url)
    print(result.content.decode())
    file_name = str(random.randint(100, 999)) + '.jpg'
    try:
        file_dir = os.path.join(path, name)
        if not os.path.exists(path):
            os.mkdir(path)
        with open(os.path.join(path, file_name), 'wb') as f:
            print('{}====={}'.format(url, name))
            f.write(result.content)
    except Exception as e:
        print(e)
        print("file_name:" + file_name + ",下载失败,url:" + url)


def load_picture_by_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            load_picture_by_url(line, file_path, line)


def load_picture_by_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            load_picture_by_file(os.path.join(root, file))
        for dir in dirs:
            load_picture_by_dir(os.path.join(root, dir))


if __name__ == '__main__':
    print(sys.argv)
    if os.path.isdir(sys.argv[1]):
        load_picture_by_dir(sys.argv[1])
    else:
        print(sys.argv[1] + "is not a usable dir!!!")
