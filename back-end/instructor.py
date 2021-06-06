import pymysql as pms
from flask import Flask
app = Flask(__name__)


# 查课表
# 有两个联系集还没建表--0516
def queryforcourse(i_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from teaches where i_id=%s" % i_id


# studentlist 学生id的列表
@app.route('/teacherchoose/')
def querystudentlist(c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select s_id from teaches where c_id ='" + c_id + "'"
    mcs.execute(find_str)
    s_list = mcs.fetchall()
    mcs.close()
    db.close()
    return s_list


# 老师挑选学生，前端返回该课程最终学生列表，插入数据库
def confirmstudent(s_list):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into student_pick(s_id, c_id, name, password)values( % s, % s, %s, %s)"
    for item in s_list:
        mcs.execute(insert_str,(s_list[i].s_id, s_list[i].c_id,s_list[i].name, s_list[i].password))
    db.commit()
    mcs.close()
    db.close()

#老师填写课程信息，插入待审核课表
def submitcourseinformation(c_id,course_name,credits,type,hour,dept_name):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into course(c_id,course_name,credits,type,hour,dept_name)values( % s, % s, %s, %s, %s, %s)"
    mcs.execute(insert_str,(c_id,course_name,credits,type,hour,dept_name))
    db.commit()
    mcs.close()
    db.close()