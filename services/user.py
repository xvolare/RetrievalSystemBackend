from models.user import User
from flask import jsonify

def user_login(username,password):
    u = User.query.filter_by(username=username).first()
    if u is None:
        # 用户不存在
        return jsonify({
            'code': -1,
            "message": "用户不存在",
            "data": ""
        })
    u_dict = u.to_dict()
    if u_dict['password'] != password:
        # 用户存在 密码错误
        return jsonify({
            'code': -2,
            "message": "密码错误",
            "data":""
        })
    return jsonify({
            'code': 0,
            "message": "登录成功",
            "data": u_dict
        })



