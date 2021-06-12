# 管理员导入学生数据信息
import pymysql as pms
from flask import Flask, jsonify, render_template, request
import json
from flask_cors import cross_origin

import maininterface
from csv import reader

app = Flask(__name__)


# 接收一个excel文件，将excel中的数据批量导入database
# excel文件需保存为csv格式，首行项分别为pid, password, name
def adminload(file):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    f = open(file, "r")
    lines = reader(f)
    for line in lines:
        if line[1] == 'password':
            continue
        maininterface.register(db, line[0], line[1], line[2], 1)
    db.commit()


# 调试示例
# dtb = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
# adminload(dtb, "mytest.csv")


def adminpasswordchange(ids, newpassword, user_class):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    if user_class == 0:
        update_str = "update student set password = '%s' where s_id= '%s'" % (newpassword, ids)
    if user_class == 1:
        update_str = "update instructor set password = '%s' where i_id= '%s'" % (newpassword, ids)
    if user_class == 2:
        update_str = "update system_manager set password = '%s' where m_id= '%s'" % (newpassword, ids)
    try:
        msg = mcs.execute(update_str)
        db.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        db.rollback()
        print('插入失败')
    finally:
        mcs.close()
        db.close()


# 利用管理员权限进行全局范围的所有表项更改（可用）
def adminchange(tablename, colunmname, primarykey, primarykeyvalue, newdata):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    if type(newdata) == int:
        update_str = "update " + tablename + " set " + colunmname + " = " + newdata + " where " \
                     + primarykey + " = '" + primarykeyvalue + "'"
    elif type(newdata) == str:
        update_str = "update " + tablename + " set " + colunmname + " = '" + newdata + "' where " \
                     + primarykey + " = '" + primarykeyvalue + "'"

    msg = mcs.execute(update_str)
    print(msg)
    db.commit()
    mcs.close()
    db.close()


# '''
# 查询待审核课程的函数的测试用例
# 已通过验证
# dbs = pms.connect(host='localhost', user='root', passwd='root', db='ccms', charset='utf8')
# mcss = dbs.cursor()
# coursel = findselectablecourse()
# print(coursel)
# '''
def findselectablecourse():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_course = "select * from course where started='待审核';"
    mcs.execute(find_course)
    courselist = mcs.fetchall()
    return courselist


# 管理员审核完成之后将课程信息插入数据库
# 此处instructor_id暂时用不上，但是前端需要将ins_id与课程信息捆绑，展示到学生选课页面中
# course表新增属性started，表示课程是否开始，若已经开始则为'已开课'，否则为'待审核'。课程开始意味着选课结束
# 管理员审核完成后将course中课程信息转移到lesson表中，并添加上课程上课的教室、时间段
@app.route('/')
@cross_origin(supports_credentials=True)
def submitcourse(c_id, year, semester, weeknumber, weekday, ts_num, building, room_num):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    update_str = "update course set started = '已开课' where c_id = '%s'" % c_id
    mcs.execute(update_str)
    find_str = "select i_id from course where c_id = '%s'" % c_id
    mcs.execute(find_str)
    i_id = list(mcs.fetchone())
    print(i_id[0])
    insert_str = "insert into teacher_rel(i_id, c_id, year, semester)value('%s','%s','%s','%s') "\
                 % (str(i_id[0]), c_id, year, semester)
    mcs.execute(insert_str)
    sqlstr = "insert into lesson(c_id, year, semester, weeknumber, weekday, time_slot_number, \
                  building, room_number,status) values ('%s','%s','%s','%s','%s','%s','%s','%s','待选课');" \
                      % (c_id, year, semester, weeknumber, weekday, ts_num, building, room_num)
    mcs.execute(sqlstr)
    db.commit()
    mcs.close()
    db.close()
    return '插入成功'


if __name__ == '__main__':
    submitcourse('jsjwl2021', 2021, 'fall', '7', '3', '5', 'A2', '402')
