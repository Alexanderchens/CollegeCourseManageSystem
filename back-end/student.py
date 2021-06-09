import pymysql as pms
from flask import Flask,jsonify
app = Flask(__name__)


# 在待选课程中插入新的学生，根据c_id索
@app.route()
def insertstudent(s_id, c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into student_pick(s_id,c_id)values(%s, %s)"

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
# 必修课按照班级分配，选修课按照学号分配
# 先获取班级名字，然后获取必修课课程
@app.route()
def getcourselist(student_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    # 根据学生id找出班级
    find_class = "select class_name from student where s_id=%s;" % student_id
    mcs.execute(find_class)
    class_name = mcs.fetchone()

    # 根据班级找出所有必修课程
    # select条件：started==1 && class_name==目标班级名称
    find_class_course = "select * from teaches where class_name=%s" % class_name
    mcs.execute(find_class_course)
    courselist = mcs.fetchall()

    t = {}
    for i in courselist:
        t[str(i)] = courselist[i]
    return jsonify(t)


@app.route()
# 查询当前可以用于选课的课程表单信息
# 学生选课界面显示可以选择的课程
def show_selectable_course():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from course where started=0;"
    mcs.execute(find_str)
    courselist = mcs.fetchall()
    t = {}
    for i in courselist:
        t[str(i)] = courselist[i]
    return jsonify(t)
