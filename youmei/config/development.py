# -*- coding:utf-8 -*-
from youmei.config.base import *
import os


DEBUG = True
ECHO_SQL = True

MAIN_DB = {
    'database_type' : 'postgresql',
    'host' : 'localhost',
    'port' : 5432,
    'user' : 'postgres',
    'password' : 'root',
    'database_name' : 'mydb'
}

