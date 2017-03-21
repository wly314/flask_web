# coding:utf-8
from youmei import application as app
from flask_script import Manager
from youmei.db_migration import create_goods_table


manager = Manager(app)


# 创建数据表
@manager.command
def db_upgrade():
    create_goods_table()


if __name__ == '__main__':
    manager.run()