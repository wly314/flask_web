# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from views import blueprint_list as blueprints
import views


BLUEPRINTS = [(views.wechat_home_bp, '/wx'), ]

def create_app(blueprints = None):
    if blueprints is None:
        blueprints = BLUEPRINTS

    app = Flask(__name__)

    wechat_configuer_blueprints(app, blueprints)

    return app


# 注册wechat应用蓝图
def wechat_configuer_blueprints(app, blueprints):
    # 注册蓝图
    if blueprints:
        for view, url_prefix in blueprints:
            app.register_blueprint(view, url_prefix = url_prefix)

application_wechat = create_app()