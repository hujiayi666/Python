from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# 创建基础类
Base = declarative_base()


# 定义Department类
class Department(Base):
    __tablename__ = 'department'
    DeptName = Column(String, primary_key=True)
    DeptAddress = Column(String)
    DeptPhone = Column(String)

    wards = relationship('Ward', back_populates='department')
    doctors = relationship('Doctor', back_populates='department')


# 定义Ward类
class Ward(Base):
    __tablename__ = 'ward'
    WardID = Column(String, primary_key=True)
    BedID = Column(String, primary_key=True)
    DeptName = Column(String, ForeignKey('department.DeptName'))

    department = relationship('Department', back_populates='wards')
    patients = relationship('Patient', back_populates='ward')


# 定义Doctor类
class Doctor(Base):
    __tablename__ = 'doctor'
    WorkID = Column(String, primary_key=True)
    DoctorName = Column(String)
    Title = Column(String)
    Age = Column(Integer)
    DeptName = Column(String, ForeignKey('department.DeptName'))

    department = relationship('Department', back_populates='doctors')
    patients = relationship('Patient', back_populates='doctor')


# 定义Patient类
class Patient(Base):
    __tablename__ = 'patient'
    PatientID = Column(String, primary_key=True)
    PatientName = Column(String)
    Gender = Column(String)
    WardID = Column(String, ForeignKey('ward.WardID'))
    BedID = Column(String, ForeignKey('ward.BedID'))
    WorkID = Column(String, ForeignKey('doctor.WorkID'))

    ward = relationship('Ward', back_populates='patients')
    doctor = relationship('Doctor', back_populates='patients')


# 创建数据库引擎
engine = create_engine('sqlite:///:memory:')  # 使用内存中的SQLite数据库

# 创建所有表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 示例数据插入
dept = Department(DeptName='Cardiology', DeptAddress='Building A', DeptPhone='123456789')
ward = Ward(WardID='W1', BedID='B1', DeptName='Cardiology')
doctor = Doctor(WorkID='D1', DoctorName='Dr. Smith', Title='Cardiologist', Age=45, DeptName='Cardiology')
patient = Patient(PatientID='P1', PatientName='John Doe', Gender='M', WardID='W1', BedID='B1', WorkID='D1')

# 将数据添加到会话中
session.add(dept)
session.add(ward)
session.add(doctor)
session.add(patient)

# 提交会话
session.commit()

