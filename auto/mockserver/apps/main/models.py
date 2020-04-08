#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import Table
from sqlalchemy import Column,String,Integer,Text,ForeignKey,Boolean,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from setting import Base

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False, index=True)
    description = Column(String(64))
    modules = relationship('Module', backref='project')
    owner_id = Column(Integer, ForeignKey('user.id'))
    members = relationship('User', secondary='project_user', backref='authorized_projects')
    createtime = Column(DateTime, default=datetime.now)
    apis = relationship('Api', backref='project')


class Module(Base):
    __tablename__ = 'module'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False, index=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    apis = relationship('Api', backref='module')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    account = Column(String(64), nullable=False, index=True)
    name = Column(String(64), index=True)
    passwd = Column(String(1024), nullable=False)
    email = Column(String(64))
    role = Column(Integer, nullable=False)
    status = Column(Boolean(), default=True)
    own_projects = relationship('Project', backref='owner')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.account)

project_user = Table(
    'project_user', Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)

class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    service_name = Column(String(128))
    uri = Column(String(256))
    request_content_type = Column(String(64))
    request_method = Column(String(64))
    description = Column(String(128))
    paras = relationship('RequestPara', backref='api')
    responseheader = relationship('ResponseHeader', backref='api')
    module_id = Column(Integer, ForeignKey('module.id'))
    project_id = Column(Integer, ForeignKey('project.id'))
    response_set = relationship('Response', backref='api')

class RequestPara(Base):
    __tablename__ = 'requestpara'
    id = Column(Integer, primary_key=True)
    order = Column(Integer,nullable=False)
    name = Column(String(64))
    match = Column(Integer,default=0)
    value = Column(String(256))
    position = Column(String(10))
    response_id = Column(Integer, ForeignKey('response.id'))
    api_id = Column(Integer, ForeignKey('api.id'))

class ResponseType(Base):
    __tablename__ = 'responsetype'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    value = Column(String(64), nullable=False)
    responses = relationship('Response', backref='type')

class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    description = Column(String(128))
    status_code = Column(Integer, default=200)
    response_content = Column(Text(10000), nullable=False)
    type_id = Column(Integer, ForeignKey('responsetype.id'))
    paras = relationship('ResponseType', backref='response')
    api_id = Column(Integer, ForeignKey('api.id'))

class ResponseHeader(Base):
    __tablename__ = 'responseheader'
    id = Column(Integer, primary_key=True)
    key = Column(String(64), nullable=False)
    value = Column(String(256), nullable=False)
    description = Column(String(128))
    api_id = Column(Integer, ForeignKey('api.id'))


class Consul(Base):
    __tablename__ = 'consul'
    id = Column(Integer, primary_key=True)
    ip = Column(String(64), nullable=False)
    port = Column(Integer,default=8500)
    desc = Column(String(128))


class RequestService(Base):
    __tablename__ = 'requestService'
    id = Column(Integer, primary_key=True)
    serviceName = Column(String(128), nullable=False)
    consul_ip = Column(String(128), nullable=False)
    consul_port = Column(String(128), nullable=False)