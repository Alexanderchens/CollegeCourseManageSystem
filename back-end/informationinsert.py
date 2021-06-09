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
