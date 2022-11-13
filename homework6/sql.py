import pymysql
import re
import numpy
import os
from os import getcwd
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData




class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = 'root'
        self.port = 3306
        self.password = '2283221488'
        self.host = '127.0.0.1'
        self.db_name = db_name
        self.connection = None
        print('here')
    def connect(self, db_created=True):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db_name if db_created else None,
                                          charset='utf8',
                                          autocommit=True,
                                          cursorclass=pymysql.cursors.DictCursor
                                          )

    def create_db(self):
        self.connect(db_created=False)
        self.connection.query(f'DROP database IF EXISTS {self.db_name}')
        self.connection.query(f'CREATE database {self.db_name}')

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_tables(self):
        self.connection.query(f'create table test1 (`id` smallint(10) not null auto_increment, `count` int(20) not null, primary key (`id`))')
        self.connection.query(
            f'create table test2 (`id` smallint(10) not null auto_increment, `method` varchar(50) not null, `count` int(20) not null, primary key (`id`))')
        self.connection.query(
            f'create table test3 (`id` smallint(10) not null auto_increment, `url` varchar(50) not null,`count` varchar(50) not null, primary key (`id`))')
        self.connection.query(
            f'create table test4 (`id` smallint(10) not null auto_increment, `url` varchar(50) not null,'
            f'`code` int(3) not null,`size` int(15) not null,`ip` varchar(50) not null, primary key (`id`))')
        self.connection.query(
            f'create table test5 (`id` smallint(10) not null auto_increment, `ip` varchar(20) not null,`count` int(15) not null, primary key (`id`))')



# r.create_db()
# r.connect()
# r.create_tables()

# r.execute_query('test_table',fetch=False)
# r.execute_query(query='test_table')


# connection = pymysql.connect(host='localhost',
#                              port=3306,
#                              user='root',
#                              password='2283221488',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


#
# connection = pymysql.connect(host='localhost',
#                              port=3306,
#                              user='root',
#                              password='2283221488',
#                              database='homework',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor,
#                              autocommit=True)
#connection.query('drop database if exists homework')
# connection.query('create database homework')
# connection.close()
# test = 'create table test_table(id int AUTO_INCREMENT, field1 varchar(32), field2 varchar(32), primary key(id))'
# connection.query(test)
# with connection.cursor() as cursor:
#     insert = f"INSERT INTO test_table(field1, field2) VALUES (%s,%s) "
#     cursor.execute(insert, ('test1', 'test21'))
#     cursor.execute(insert, ('test2', 'test22'))
#     cursor.execute(insert, ('test3', 'test23'))
#
#     everything = "SELECT * FROM test_table"
#     cursor.execute(everything)
#     rows = cursor.fetchall()
#     print(rows)

