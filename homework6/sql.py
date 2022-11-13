import pymysql
import re
import numpy
import os
dir = r'./files/'
os.chdir(dir)
nginx_re = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+) - - (?P<datetime>\[.+\]) \"(?P<method>\w+) (?P<url>.+?) (?P<protocol>.+?)\" (?P<responce>\d+) (?P<size>\d+)")
log = []
exclude = 0
with open("access.logs") as f:
    for row in f.readlines():
        if parsed := nginx_re.findall(row):
            log.append(parsed)
        else:
            exclude += 1

class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = 'root'
        self.port = 3306
        self.password = '0000'
        self.host = '127.0.0.1'
        self.db_name = db_name
        self.connection = None

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
        cursor = self.connection.cursor()
        cursor.execute(query)
        if fetch:
            return cursor.fetchall()

    def log_len(self):
        exclude = 0
        with open("access.logs") as f:
            for row in f.readlines():
                if parsed := nginx_re.findall(row):
                    log.append(parsed)
                else:
                    exclude += 1
        return log, exclude

    def methods_counting(self):
        count, post, get, head, put, other = 0, 0, 0, 0, 0, 0
        methods = ["POST", "GET", "HEAD", "PUT", "OTHER"]
        for i in range(len(log)):
            count += 1
            if log[i][0][2] == methods[0]:
                post += 1
            elif log[i][0][2] == methods[1]:
                get += 1
            elif log[i][0][2] == methods[2]:
                head += 1
            elif log[i][0][2] == methods[3]:
                put += 1
            else:
                other += 1
        counts=[post, get, head, put, other]
        return counts, methods

    def url_counting(self, count):
        buf = []
        counter = []
        for i in range(len(log)): buf.append(log[i][0][3])
        uniq = numpy.unique(buf)
        for i in range(len(uniq)):
            if buf.count(uniq[i]) > 1000: counter.append(buf.count(uniq[i]))
        counter.sort()
        return buf, uniq, counter

    def mock_info(self):
        mock = []
        with open("files/mock.txt") as f:
            for row in f.readlines():
                buf = row.split()
                mock.append(buf)
        return mock

    def ip_counting(self):
        ips = []
        ips_counter = []
        for i in range(len(log)):
            if log[i][0][5] == "500": ips.append(log[i][0][0])
        uniq_ips = numpy.unique(ips)
        for i in range(len(uniq_ips)):
            ips_counter.append(ips.count(uniq_ips[i]))
            if ips_counter[i] > min(ips_counter): print(uniq_ips[i], '\n', ips_counter[i])
        return uniq_ips, ips_counter, ips

    def create_tables(self):
        self.connection.query(f'create table test1 (`id` smallint(10) not null auto_increment, `count` int(20) not null, primary key (`id`))')
        self.connection.query(
            f'create table test2 (`id` smallint(10) not null auto_increment, `method` varchar(50) not null, `count` int(20) not null, primary key (`id`))')
        self.connection.query(
            f'create table test3 (`id` smallint(10) not null auto_increment, `url` varchar(50) not null,`count` varchar(50) not null, primary key (`id`))')
        self.connection.query(
            f'create table test4 (`id` smallint(10) not null auto_increment, `ip` varchar(50) not null,'
            f'`code` int(3) not null,`size` int(15) not null,`url` varchar(200) not null, primary key (`id`))')
        self.connection.query(
            f'create table test5 (`id` smallint(10) not null auto_increment, `ip` varchar(20) not null,`count` int(15) not null, primary key (`id`))')

    def show_db(self):
        print(self.connection.query(f'show databases'))
