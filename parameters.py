#!/usr/bin/env python3
# encoding: utf-8

import platform

r"""
一些初始参数的设置，路径相关需要修改为自动获取
"""
version='1.0.1.20171220_Alpha'
class client():
    system=platform.system()
    if system=='Linux':
        path="/home/xhq/Papers"
        chrome="evince"
    elif system=='Windows':
        path="C:\XLIB\Papers"
        chrome="C:/Users/xhq/AppData/Local/Google/Chrome/Application/chrome.exe"
    else:
        path="./"
    title='.'.join(["论文管理 v",version])
    
