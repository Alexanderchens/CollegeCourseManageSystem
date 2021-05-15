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

@app.route()
def getcourselist():
    db = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcs = db.cursor()
    find_str = "select * from course"
    mcs.execute(find_str)
    courselist = mcs.fetchall()
    t = {}
    for i in courselist:
        t[str(i)] = courselist[i]
    return jsonify(t)

