import pymysql as pms
from flask import Flask,jsonify
app = Flask(__name__)


@app.route()
def insertstudent(s_id, c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into t_student(s_id,c_id)values( % s, % s)"

    try:
        mcs.execute(insert_str, (s_id, c_id))
        db.commit()
        print('插入成功')
        success = True
    except Exception as e:
        print(e)
        db.rollback()
        print('插入失败')
        success = False
    finally:
        mcs.close()
        db.close()
        return success


# 查询当前学生已经拥有的课程
@app.route()
def getcourselist(student_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_class =
    find_str = "select * from course where started=1;"
    mcs.execute(find_str)
    courselist = mcs.fetchall()
    t = {}
    for i in courselist:
        t[str(i)] = courselist[i]
    return jsonify(t)


@app.route()
# 查询当前可以用于选课的课程表单信息
def showselectablecourse():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from course where started=0;"
    mcs.execute(find_str)
    courselist = mcs.fetchall()
    t = {}
    for i in courselist:
        t[str(i)] = courselist[i]
    return jsonify(t)