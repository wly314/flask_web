# coding:utf-8
from flask import Blueprint, render_template


wechat_home_bp = Blueprint('wechat_home', __name__, template_folder='ym_wechat/templates', static_folder='static')


@wechat_home_bp.route('/')
def index():
    return render_template('home/wechat_index.html',
                    title = 'Hello')