# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from youmei.config import setting
from flask_sqlalchemy import SQLAlchemy
from views import blueprint_list as blueprints


def create_app():
    app = Flask(__name__)

    app.config.from_object(setting)
    configuer_blueprints(app, blueprints)

    return app

# 注册youmei应用蓝图
def configuer_blueprints(app, blueprints):
    # 注册蓝图
    if blueprints:
        for view, url_prefix in blueprints:
            app.register_blueprint(view, url_prefix = url_prefix)


application = create_app()