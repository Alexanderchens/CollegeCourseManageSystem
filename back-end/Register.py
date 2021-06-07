# 注册
# 先检查user表中有没有已经创建的用户，如果有则返回用户名重复，无则insert

import pymysql as pms
from flask import Flask, jsonify
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
            return False
    elif user_class == 2:
        find_str = "SELECT * FROM instructor WHERE i_id = '%s'" % ids
        mcs.execute(find_str)
        data = mcs.fetchone()
        if data is None:
            exe_str = "INSERT INTO instructor(i_id, name, password) VALUES ('%s','%s','%s')" % (ids, name, password)
        else:
            return False
    elif user_class == 3:
        find_str = "SELECT * FROM system_manager WHERE m_id = '%s'" % ids
        mcs.execute(find_str)
        data = mcs.fetchone()
        if data is None:
            exe_str = "INSERT INTO system_manager(m_id, name, password) VALUES ('%s','%s','%s')" % (ids, name, password)
        else:
            return False
    mcs.execute(exe_str)
    db.commit()
    db.close()
    return True


# 调试示例
# dtb = pms.connect("localhost", "root", "root", "CollegeCourseManageSystem")
# register(dtb, '201930390029', 'cocoa', 'cc', 1)
