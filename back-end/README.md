后端任务：
    （Initialization.py）初始化数据库：
        检查当前是否存在collegecoursemanagesystem
            若存在，则返回
            若不存在，则调用建库的sql文件进行建库

    (Register)注册：
        传入“username”和“password”两个字符串
        向数据库查询username是否已经存在，
            若存在则返回异常信息，若不存在则insert

    (LoginCheck)登录验证：
        前端传回“username”和“password”两个字符串
        利用sql向数据库查询并返回判定结果

    (AdminUpdate)管理员修改：
      判断当前操作者身份（由前端记录并返回当前操作者状态）
      若当前身份是管理员，则允许执行以下操作：
        (AdminLoad)管理员录入学生信息：
            管理员传递一个excel文件，前端将excel文件传递到后端。
            后端根据收到的excel，将学生信息进行批量插入，以及学生账号批量创建

        (AdminPasswordChange)管理员修改学生登录密码：
            修改指定学生的密码（根据username查询并修改密码）

        (AdminInsert)插入数据：
            从前端传入数据，判断数据并调用相应函数进行数据库数据插入操作
              数据可能的格式（字符串元组，excel文件）(所有返回的元组必须包含)

        (AdminChange)修改数据：
            前端返回（


course表中的started，取1时表示选上的必修课和选修课，取0时表示未选上的选修课


学生课表查询函数

教

管理员查看未审核的临时课程

