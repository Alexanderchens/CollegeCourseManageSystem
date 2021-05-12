# 用于初始化数据库
# 检测系统中是否有数据库
# 若无则调用‘initialization_commands.txt’中的预置sql命令进行数据库初始建库

# 逐行读取，然后execute
import pymysql as pms


# 数据库初始化
def init(database, file):
    with open(file, "r") as f:
        data = f.read()
        lines = data.splitlines()
        sql_data = ''
        # 将--注释开头的全部过滤，将空白行过滤
        for line in lines:
            if len(line) == 0:
                continue
            elif line.startswith("--"):
                continue
            else:
                sql_data += line
        sql_list = sql_data.split(';')[:-1]
        sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
    mycs = db.cursor()
    for item in sql_list:
        mycs.execute(item)


# 初始化调试示例
db = pms.connect("localhost", "root", "root")
cs = db.cursor()
cs.execute("SHOW DATABASES")
data = cs.fetchall()
print(data)

flag = True
for row in data:
    if row[0] == "collegecoursemanagesystem":
        flag = False
        break
if flag:
    init(db,"initialization.sql")
    db.commit()

db.close()
