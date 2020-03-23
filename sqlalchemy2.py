from sqlalchemy1 import Session, Departments, Employees, Salary

# 创建一个会话实例
session = Session()

# 增
hr = Departments(dep_id=1, dep_name='人事部' )
cw = Departments(dep_id=2, dep_name='财务部' )
ops = Departments(dep_id=3, dep_name='运维部' )
dev = Departments(dep_id=4, dep_name='开发部' )
qa = Departments(dep_id=5, dep_name='测试部' )
market = Departments(dep_id=6, dep_name='市场部' )
session.add(hr)   # 插入一条记录
session.add_all([cw, ops, dev, qa, market])  # 同时插入多条记录

# 查
# 查询时，使用类名作为查询条件，返回的是实例集合
qset1 = session.query(Departments)
print(qset1)
for dep in qset1:
    print(dep.dep_id, dep.dep_name)
# 查询时，使用变量名作为查询条件，返回的是元组
qset2 = session.query(Departments.dep_id, Departments.dep_name)
for data in qset2:
    print(data)
# 排序
qset3 = session.query(Departments).order_by(Departments.dep_id)
for i in qset3:
    print(i.dep_id, i.dep_name)
# 过滤
qset4 = session.query(Departments).filter(Departments.dep_id > 2)
for i in qset4:
    print(i.dep_id, i.dep_name)
# 叠加过滤
qset5 = session.query(Departments).filter(Departments.dep_id > 2).filter(Departments.dep_id < 5)
for i in qset5:
    print(i.dep_id, i.dep_name)
# %
qset6 = session.query(Departments).filter(Departments.dep_name.like('%事%'))
for i in qset6:
    print(i.dep_id, i.dep_name)
# 查询id为1，3，5的部门
qset7 = session.query(Departments).filter(Departments.dep_id.in_([1, 3, 5]))
for i in qset7:
    print(i.dep_id, i.dep_name)
# 查询id不是1，3，5的部门
qset8 = session.query(Departments).filter(~Departments.dep_id.in_([1, 3, 5]))
for i in qset8:
    print(i.dep_id, i.dep_name)
# 多表查询，query参数先写Employees.xxx，join时，参数为Departments
# 如果query参数先写Departments.xxx, join时，参数就是Employee
qset9 = session.query(Employees.emp_name, Departments.dep_name).join(Departments)
for data in qset9:
    print(data)
# 从查询结果中取出数据
# all方法取出所有数据，构成列表
# first取出数据的第一个结果
qset10 = session.query(Departments.dep_name, Employees.emp_name).join(Employees)
print(qset10.all())
print(qset10.first())

# 改
qset11 = session.query(Departments).filter(Departments.dep_name == '人事部')
hr = qset11.first()
hr.dep_name = '人力资源部'

# 删
qset12 = session.query(Departments).filter(Departments.dep_name == '市场部')
market = qset12.first()
session.delete(market)

# 确认
session.commit()

# 关闭会话
session.close()
