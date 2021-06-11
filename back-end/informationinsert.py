# 插入一些教室和时间槽之类的基本信息
import pymysql as pms


# 成功
def inserttimeslot():
    dbs = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcss = dbs.cursor()
    for weeknumber in range(20):
        for weekday in range(7):
            for timesn in range(11):
                ins_str = "insert into time_slot(weeknumber,weekday,time_slot_number) values (%s,%s,%s)" \
                          % (str(weeknumber+1), str(weekday+1), str(timesn+1))
                mcss.execute(ins_str)
    dbs.commit()
    dbs.close()
    mcss.close()


# 教室插入
# 成功
def insertclassroom():
    dbs = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcss = dbs.cursor()
    for i in range(5):
        building = 'A'+str(i+1)
        for lou in range(1, 6, 1):
            for fang in range(1, 9, 1):
                fanghao = str(lou)+'0'+str(fang)
                ins_fang = "insert into classroom(building,room_number) values ('%s','%s')" % (building, fanghao)
                mcss.execute(ins_fang)
    dbs.commit()
    dbs.close()
    mcss.close()


# insertclassroom()
# inserttimeslot()
def insertdept():
    li = ['机械与汽车工程学院','建筑学院','土木与交通学院','电子与信息学院','材料科学与工程学院','化学与化工学院','轻工科学与工程学院',
        '食品科学与工程学院','数学学院','物理与光电学院','经济与金融学院','旅游管理系','电子商务系','自动化科学与工程学院','计算机科学与工程学院',
        '电力学院','生物科学与工程学院','环境与能源学院','软件学院','工商管理学院','公共管理学院','马克思主义学院','外国语学院','法学院',
        '新闻与传播学院','艺术学院','体育学院','设计学院','医学院','国际教育学院','生物医学科学与工程学院','吴贤铭智能工程学院','分子科学与工程学院',
        '微电子学院','未来技术学院']
    dbs = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcss = dbs.cursor()
    for i in li:
        ins = "insert into department(dept_name) value ('%s')" % i
        mcss.execute(ins)
    dbs.commit()
    dbs.close()
    mcss.close()


def insertinstructor():
    dbs = pms.connect(host='localhost', user='root', passwd='root', db='collegecoursemanagesystem', charset='utf8')
    mcss = dbs.cursor()
    dbs.commit()
    dbs.close()
    mcss.close()
