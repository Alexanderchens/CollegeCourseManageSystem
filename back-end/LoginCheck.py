# 登录确认
import pymysql as pms


# 参数分别为：数据库 id 密码
# 分别向三个库查找id
# 失败时返回false
# 成功时返回[id，user_class]
def logincheck(db, ids, password):
    mycursor = db.cursor()
    exe_str = "SELECT PASSWORD FROM student WHERE s_id='%s'" % ids
    mycursor.execute(exe_str)
    data = mycursor.fetchone()
    user_class = 0
    if data is None:
        exe_str = "SELECT PASSWORD FROM instructor WHERE i_id='%s'" % ids
        mycursor.execute(exe_str)
        data = mycursor.fetchone()
    else:
        user_class = 1

    if data is None:
        exe_str = "SELECT PASSWORD FROM system_manager WHERE m_id='%s'" % ids
        mycursor.execute(exe_str)
        data = mycursor.fetchone()
    else:
        user_class = 2
    if data is None:
        return False
    else:
        user_class = 3
    ss = data[0]
    print(ss)
    if ss == password:
        a = [id, user_class]
        return a
    else:
        return False


# 调试示例
dtb = pms.connect("localhost", "root", "root", "CollegeCourseManageSystem")
mcs = dtb.cursor()
ins = "INSERT INTO student(s_id,password) VALUES ('20193039', 'cocoa');"
mcs.execute(ins)
if logincheck(dtb, '20193039', 'cocoa'):
    print('success')
else:
    print('what a fail')