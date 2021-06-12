import json

import pymysql as pms
from flask import Flask, jsonify
from flask_cors import cross_origin

app = Flask(__name__)


# 在待选课程中插入新的学生，根据c_id索
@app.route('/')
@cross_origin(supports_credentials=True)
def insert_student(s_id, c_id, i_id, year, semester):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into student_pick(s_id,c_id,i_id,year,semester,status)values(%s,%s,%s,%s,%s,%s)"
    if check_time_free(s_id, c_id):
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
    else:
        return '时间冲突'
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
# 2.课表查询函数
@app.route()
@cross_origin(supports_credentials=True)
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


# dst = getcourselist('201930390029')
# print(dst, '????')
# 四舍五入算通过了


# 3.查询可选择的课表函数
# 要从lesson中查询，因为只有lesson中包含有上课时间段的信息
# print(show_selectable_course())
# 已验证通过
@app.route('/')
@cross_origin(supports_credentials=True)
def show_selectable_course():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from lesson where status='选课中';"
    mcs.execute(find_str)
    courselist = list(mcs.fetchall())
    return courselist


# 根据时间段查找对应的课程列表
@app.route('/')
@cross_origin(supports_credentials=True)
def find_time_courselist(weeknumber, weekday, time_slot_number):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_exe = "select c_id from coursetime where weeknumber=%s and weekday=%s and time_slot_number=%s" \
               % (weeknumber, weekday, time_slot_number)
    mcs.execute(find_exe)
    courselist = list(mcs.fetchall())
    db.close()
    mcs.close()
    return courselist


# 根据已有课程查空教室
def find_empty_classroomlist(course_list):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    classroomlist = []
    for i in range(5):
        building = 'A'+str(i+1)
        for lou in range(1, 6, 1):
            for fang in range(1, 9, 1):
                fanghao = str(lou)+'0'+str(fang)
                classroom = [building, fanghao]
                classroomlist.append(classroom)
    print(classroomlist)
    for c_id in course_list:
        find_classroom = "select building,room_number from lesson where c_id='%s'" \
                         "and status='已开课';" \
                         % (str(c_id[0]))
        print(find_classroom)
        mcs.execute(find_classroom)
        now = list(mcs.fetchone())
        print(now)
        classroomlist.remove(now)
    db.close()
    mcs.close()
    return classroomlist


# 根据时间段查找空教室
@app.route('/')
@cross_origin(supports_credentials=True)
def find_time_empty_classroomlist(weeknumber, weekday, time_slot_number):
    courselist = find_time_courselist(weeknumber, weekday, time_slot_number)
    c_list = find_empty_classroomlist(courselist)
    return json.dumps({'emptyclassroomlist': c_list})


# 查询对应课程是否与该学生所选课程有时间冲突
@app.route('/')
@cross_origin(supports_credentials=True)
def check_time_free(s_id, c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    courselist = getcourselist(s_id)
    if len(courselist)!=0:
        slot_list = []
        for item in courselist:
            find_str = "select * from ((select weeknumber, weekday, time_slot_number from coursetime where c_id ='%s')"\
                " tb1 natural join " \
             "(select weeknumber, weekday, time_slot_number from coursetime where c_id = '%s') tb2)" % (item[0], c_id)
            mcs.execute(find_str)
            slot_list = mcs.fetchall()
            print(slot_list)
            if len(slot_list) != 0:
                return False
        print(slot_list)
    return True

# print(find_time_empty_classroomlist(1, 1, 1))
# 已通过
