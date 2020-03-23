from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据库名?参数
    'mysql+pymysql://root:123456@192.168.4.52/tedu1910?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上打印debug日志，生产环境不要打开
)

# 如果需要对数据库进行增删改查，需要创建到服务器的会话
Session = sessionmaker(bind=engine)

# 创建实体类的基类，固定写法
Base = declarative_base()


# 创建实体类
class Departments(Base):
    __tablename__ = 'departments'  # 与库中哪张表映射
    dep_id = Column(Integer, primary_key=True)  # 每个字段都是一个Column
    dep_name = Column(String(20))

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 库中无表则创建，有表不会创建
