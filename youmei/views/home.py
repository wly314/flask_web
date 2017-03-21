# coding:utf-8
from flask import Blueprint, render_template, jsonify
from youmei.models.goods import Goods
from youmei.models.session import session_cm


home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home_bp.route('/')
def index():
    with session_cm() as index_session:

        ar = index_session.query(Goods).all()
        # if not ar:
        #     res = {'error':'no data'}
        #     return jsonify(res)
        for good in ar:
            print (good.id)
            print (good.name)
    return render_template('home/index.html',
                           title = 'Hello')