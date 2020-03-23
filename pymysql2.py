'''增删改查'''
import pymysql

#建立到数据库的连接
conn = pymysql.connect(
    host='192.168.4.52', port=3306, user='root',
    password='123456', db='nsd1910', charset='utf8'
)

#创建游标
cur = conn.cursor()

#编写sql语句
#增
insert_dep = 'insert into departments values (%s, %s)'
cur.execute(insert_dep, (1, '人事部'))
cur.executemany(
    insert_dep,
    [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '市场部'), (6, '财务部')]
)
#查
select1 = 'select * from departments'
cur.execute(select1)
decord1 = cur.fetchone() #取出第一条查询结果
print(decord1)
decord2 = cur.fetchmany(2) #继续取出两条查询结果
print(decord2)
decord3 = cur.fetchall() #继续取出剩余所有结果
print(decord3)
#改
update1 = 'update departments set dep_name=%s where dep_name=%s'
cur.execute(update1, ('人力资源部', '人事部'))
#删
delete1 = 'delete from departments where dep_id=%s'
cur.execute(delete1, (6, ))

#确认
conn.commit()

#关闭
cur.close()
conn.close()