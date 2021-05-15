# 管理员导入学生数据信息
import pymysql as pms
import Register
from csv import reader


# 接收一个excel文件，将excel中的数据批量导入database
def adminload(db, file):
    f = open(file, "r")
    lines = reader(f)
    for line in lines:
        if line[1] == 'password':
            continue
        Register.register(db, line[0], line[1], line[2], 1)
    db.commit()


# 调试示例
dtb = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
adminload(dtb, "mytest.csv")


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


# 管理员审核完成之后将课程信息插入数据库
# 未完成
def submitcourse(course_id, name, hour, credit, course_type, ins_id):
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()