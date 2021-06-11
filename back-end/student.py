import pymysql as pms
from flask import Flask,jsonify
app = Flask(__name__)


# 在待选课程中插入新的学生，根据c_id索
@app.route()
def insert_student(s_id, c_id, i_id, year, semester):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into student_pick(s_id,c_id,i_id,year,semester,status)values(%s,%s,%s,%s,%s,%s)"

    try:
        mcs.execute(insert_str, (s_id, c_id, i_id, year, semester, "未选上"))
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
# test for insert_student()


'''
str1 = '茶与咖啡评鉴'
# insert_student(201930390029, 'cykfjs2021', 19151234446, 2021, 'fall')
dbs = pms.connect(host='localhost', user='root', passwd='root', db='ccms', charset='utf8')
mcss = dbs.cursor()
mcss.execute('select * from student_pick;')
stulist = mcss.fetchall()
print(stulist)
'''


# 查询当前学生已经拥有的课程
# 必修课按照班级分配，选修课按照学号分配
# 先获取班级名字，然后获取必修课课程
@app.route()
# 2.课表查询函数
def getcourselist(student_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    # 根据学生id找出班级
    find_class = "select class_name from student where s_id=%s;" % student_id
    mcs.execute(find_class)
    dt = mcs.fetchone()
    class_name = str(dt[0])
    # print(class_name)
    # 根据班级找出所有必修课程
    find_class_course = "select c_id,i_id from teaches where class_name='%s'" % class_name
    mcs.execute(find_class_course)
    c_id_and_i_id_list = mcs.fetchall()
    # print(c_id_and_i_id_list)
    courselist = []
    for row in c_id_and_i_id_list:
        cid = str(row[0])
        find_compulsory = "select * from lesson where c_id='%s'" % cid
        mcs.execute(find_compulsory)
        lesson = list(mcs.fetchone())
        lesson.append(str(row[1]))
        # print(lesson)
        courselist.append(lesson)
    find_optional_cid = "select c_id,i_id from student_pick where s_id='%s' and status='%s';" % (student_id, "已选上")
    mcs.execute(find_optional_cid)
    c_id_list = list(mcs.fetchall())
    for tmp in c_id_list:
        cid = str(tmp[0])
        iid = str(tmp[1])
        find_optional = "select * from lesson where c_id='%s';" % cid
        mcs.execute(find_optional)
        lesson = list(mcs.fetchone())
        lesson.append(iid)
        courselist.append(lesson)
    return courselist


dst = getcourselist('201930390029')
# print(dst, '????')
# 四舍五入算通过了


@app.route()
# 3.查询可选择的课表函数
# 要从lesson中查询，因为只有lesson中包含有上课时间段的信息
# print(show_selectable_course())
# 已验证通过
def show_selectable_course():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from lesson where status='选课中';"
    mcs.execute(find_str)
    courselist = list(mcs.fetchall())
    return courselist
