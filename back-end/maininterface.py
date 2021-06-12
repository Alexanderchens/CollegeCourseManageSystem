# 注册
# 先检查user表中有没有已经创建的用户，如果有则返回用户名重复，无则insert
import pymysql as pms
from flask import Flask, jsonify, render_template, request
import json

from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register(db, ids, password, name, user_class):
    mcs = db.cursor()
    if user_class == 1:
        find_str = "SELECT * FROM student WHERE s_id = '%s'" % ids
        mcs.execute(find_str)
        data = mcs.fetchone()
        if data is None:
            exe_str = "INSERT INTO student(s_id, name, password) VALUES ('%s','%s','%s')" % (ids, name, password)
        else:
            return json.dumps({'IsSuccess': 'false'})
    elif user_class == 2:
        find_str = "SELECT * FROM instructor WHERE i_id = '%s'" % ids
        mcs.execute(find_str)
        data = mcs.fetchone()
        if data is None:
            exe_str = "INSERT INTO instructor(i_id, name, password) VALUES ('%s','%s','%s')" % (ids, name, password)
        else:
            return json.dumps({'IsSuccess': 'false'})
    elif user_class == 3:
        find_str = "SELECT * FROM system_manager WHERE m_id = '%s'" % ids
        mcs.execute(find_str)
        data = mcs.fetchone()
        if data is None:
            exe_str = "INSERT INTO system_manager(m_id, name, password) VALUES ('%s','%s','%s')" % (ids, name, password)
        else:
            return json.dumps({'IsSuccess': 'false'})
    mcs.execute(exe_str)
    db.commit()
    db.close()
    return json.dumps({'IsSuccess': 'true'})


# 调试示例
# dtb = pms.connect("localhost", "root", "root", "CollegeCourseManageSystem")
# register(dtb, '201930390029', 'cocoa', 'cc', 1)


# 登录确认
# 参数分别为：数据库 id 密码
# 分别向三个库查找id
# 失败时返回false
# 成功时返回[id，user_class]
@app.route('/logincheck', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def logincheck():
    db = pms.connect("localhost", "root", "root", "CollegeCourseManageSystem")
    mycursor = db.cursor()
    data = request.get_json()
    ids = data['username']
    password = data['password']
    exe_str = "SELECT PASSWORD FROM student WHERE s_id='%s'" % ids
    mycursor.execute(exe_str)
    data = mycursor.fetchone()
    user_class = 0
    if data is None:
        exe_str = "SELECT PASSWORD FROM instructor WHERE i_id='%s'" % ids
        mycursor.execute(exe_str)
        data = mycursor.fetchone()
    else:
        user_class = 1

    if data is None:
        exe_str = "SELECT PASSWORD FROM system_manager WHERE m_id='%s'" % ids
        mycursor.execute(exe_str)
        data = mycursor.fetchone()
    else:
        user_class = 2
    if data is None:
        return json.dumps({'IsSuccess': 'false'})
    else:
        user_class = 3
    ss = data[0]
    print(ss)
    if ss == password:
        return json.dumps({'IsSuccess': 'true'})
    else:
        return json.dumps({'IsSuccess': 'false'})


# 调试示例
'''
dtb = pms.connect("localhost", "root", "root", "CollegeCourseManageSystem")
mcs = dtb.cursor()
ins = "INSERT INTO student(s_id,password) VALUES ('20193039', 'cocoa');"
mcs.execute(ins)
if logincheck(dtb, '20193039', 'cocoa'):
    print('success')
else:
    print('what a fail')
'''
if __name__ == '__main__':
    app.run()
