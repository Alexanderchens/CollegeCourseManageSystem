# 用于初始化数据库
# 检测系统中是否有数据库
# 若无则调用‘initialization_commands.txt’中的预置sql命令进行数据库初始建库

# 逐行读取，然后excute
import mysql.connector


def init(mycursor):
    for line in open("initialization_commands.txt"):
        mycursor.excute(line)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
flag = True
for x in mycursor:
    if(x == "CollegeCourseManageSystem"):
        flag = False
if flag:
    init(mycursor)
