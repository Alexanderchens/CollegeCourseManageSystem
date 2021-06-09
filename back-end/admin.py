# 管理员导入学生数据信息
import pymysql as pms
import maininterface
from csv import reader


# 接收一个excel文件，将excel中的数据批量导入database
# excel文件需保存为csv格式，首行项分别为pid, password, name
def adminload(db, file):
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
    if user_class == 3:
        update_str = "update system_manager set password = '%s' where m_id= '%s'" % (newpassword, ids)
        msg = mcs.execute(update_str)
        if msg != 1:
            print("faild executed!")
    if user_class == 2:
        update_str = "update instructor set password = '%s' where i_id= '%s'" % (newpassword, ids)
        msg = mcs.execute(update_str)
        if msg != 1:
            print("faild executed!")
    if user_class == 1:
        update_str = "update student set password = '%s' where s_id= '%s'" % (newpassword, ids)
        msg = mcs.execute(update_str)
        if msg != 1:
            print("faild executed!")
    db.commit()
    mcs.close()
    db.close()


# 利用管理员权限进行全局范围的所有表项更改
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
def submitcourse(course_id, course_name, hour, credit, course_type, dept_name):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    sqlstr = "insert into course(c_id,course_name,credits,type,hour,dept_name,started) values (%s,%s,%s,%s,%s,%s,0);"\
             % (course_id, course_name, credit, course_type, hour, dept_name)
    mcs.execute(sqlstr)
    db.commit()
    mcs.close()
    db.close()

