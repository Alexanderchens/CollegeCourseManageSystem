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

