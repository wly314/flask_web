# coding:utf-8
from home import wechat_home_bp


# 创建一个Blueprint列表，以便循环导入注册蓝图
blueprint_list = [(wechat_home_bp, '/wx'),]