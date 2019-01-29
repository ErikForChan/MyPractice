#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/21 18:46
# software: PyCharm
import json


def write_dict_into_file(path,dict):
    with open(path, 'w', encoding='UTF-8') as userFile:
        userFile.writelines(json.dumps(dict) + "\n")
