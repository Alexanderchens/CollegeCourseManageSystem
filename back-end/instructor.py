import pymysql as pms
from flask import Flask

app = Flask(__name__)


# 查课表（已测试）
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
    return c_list


# studentlist 学生id的列表（已测试）
# @app.route('/teacherchoose/')
def querystudentlist(c_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from student_pick where c_id ='" + c_id + "' and status = '未选上' "
    mcs.execute(find_str)
    s_list = list(mcs.fetchall())
    mcs.close()
    db.close()
    return s_list


# 老师挑选学生，前端返回该课程最终学生列表，插入数据库（已测试）
def confirmstudent(s_list):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    update_str = "update student_pick set status = '已选上' where s_id = %s"
    for item in s_list:
        mcs.execute(update_str, item)
    db.commit()
    mcs.close()
    db.close()


# 老师填写课程信息，插入待审核课表(已测试)
def submitcourseinformation(c_id, course_name, credits, type, hour, dept_name):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    insert_str = "insert into course(c_id, course_name, credits, type, hour, dept_name, started)" \
                 "values( %s, %s, %s, %s, %s, %s, '待审核')"
    mcs.execute(insert_str, (c_id, course_name, credits, type, hour, dept_name))
    db.commit()
    mcs.close()
    db.close()


if __name__ == '__main__':
    s_List = queryforcourse('209382')
    print(s_List[0])
