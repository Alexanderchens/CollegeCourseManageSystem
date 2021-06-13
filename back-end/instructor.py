import json

import pymysql as pms
from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)


# 查课表（已测试）
@app.route('/')
@cross_origin(supports_credentials=True)
def queryforcourse(i_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from teacher_rel natural join lesson where i_id= '" + i_id + "' "
    mcs.execute(find_str)
    c_list = list(mcs.fetchall())
    # for item in cid_list:
    #     find_str = "select * from lesson where c_id = '" + item + "' "
    #     mcs.execute(find_str)
    #     c_list += mcs.fetchall()
    mcs.close()
    db.close()
    return json.dumps({'teacherCourse': c_list})


# studentlist 学生id的列表（已测试）
@app.route('/teacherchoose/')
@cross_origin(supports_credentials=True)
def querystudentlist(c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from student_pick where c_id ='" + c_id + "' and status = '未选上' "
    mcs.execute(find_str)
    s_list = list(mcs.fetchall())
    mcs.close()
    db.close()
    return json.dumps({'studentList': s_list})


# 老师挑选学生，前端返回该课程最终学生列表，插入数据库（已测试）
@app.route('/')
@cross_origin(supports_credentials=True)
def confirmstudent():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()

    data = request.get_json()
    s_list = data['s_list']
    i_id = data['i_id']
    c_id = data['c_id']

    update_str = "update student_pick set status = '已选上' where s_id ='%s' and i_id='%s' and c_id='%s'"
    for item in s_list:
        mcs.execute(update_str, (item, i_id, c_id))
    db.commit()
    mcs.close()
    db.close()


# 老师填写课程信息，插入待审核课表(已测试)
@app.route('/')
@cross_origin(supports_credentials=True)
def submitcourseinformation(c_id, course_name, cre, ty, hour, dept_name):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into course(c_id, course_name, credits, type, hour, dept_name, started)" \
                 "values( %s, %s, %s, %s, %s, %s, '待审核')"
    mcs.execute(insert_str, (c_id, course_name, cre, ty, hour, dept_name))
    db.commit()
    mcs.close()
    db.close()


if __name__ == '__main__':
    s_List = queryforcourse('209382')
    print(s_List[0])
