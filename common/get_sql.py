from config.sql_cofg import sql_conf

def getsql(sql):
    # 创建游标
    corror=sql_conf().cursor()
    # 运行sql
    corror.execute(sql)
    # 保存sql结果
    data = corror.fetchall()
    # 关闭游标
    corror.close()
    # 关闭数据库
    sql_conf().close()
    return data
#sql='select * from mydatabase.student'
#print(getsql(sql)[1][1])
