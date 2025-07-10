import pymysql

### 方法一：普通方法，连接数据库，进行参数化
host='localhost'
user='YR'
password ='123456'
port =3306
charset = 'utf8'

# 连接数据库
conn = pymysql.connect(host=host, user=user, password=password, port=port,charset=charset)
sql = 'select id,Sname,age,sex from mydatabase.student'
# 建立游标
cursor = conn.cursor()
# 运行sql语句
cursor.execute(sql)
# 保存sql数据给data变量
data = cursor.fetchall()
# 关闭游标
cursor.close
# 关闭数据库
conn.close()
# data_list = list(data)
# 元组类型 获取第二组数据中的第二个值
print(data[0][1])

# 方法二：封装数据库，前期配置，和在common模块封装运行数据库

def sql_conf():
    host,user,password,port,charset=['localhost','YR','123456',3306,'utf8']
    conn = pymysql.connect(host=host, user=user, password=password, port=port, charset=charset)
    return conn


