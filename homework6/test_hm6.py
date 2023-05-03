import pytest
from sql import MysqlClient


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client


class TestMysql(MyTest):

    def test_len(self):
        info = self.client.log_len()
        self.client.execute_query(fetch=True, query=f'insert into test1 (count) values ({info})')
        assert info == self.client.read('*', 'test1')[0]['count']

    def test_count_method(self):
        info = self.client.methods_counting()
        for i in range(len(info[0])):
            self.client.execute_query(fetch=True, query=f'insert into test2 (method,count)'
                                                        f' values ("{info[0][i]}","{info[1][i]}")')
        for i in range(len(info[0])):
            assert self.client.read('*', 'test2')[i]['method'] == info[0][i] and self.client.read('*', 'test2')[i][
                'count'] == info[1][i]

    def test_count_url(self, count=10):
        buffer0 = []
        buffer1 = []
        info = self.client.url_counting(count)
        for i in range(len(info[1])):
            if info[0].count(info[1][i]) >= min(info[2][-count:]):
                buffer0.append(info[1][i])
                buffer1.append(str(info[0].count(info[1][i])))
                self.client.execute_query(fetch=True, query=f'insert into test3 (url,count)'
                                                            f' values ("{info[1][i]}","{info[0].count(info[1][i])}")')
        for i in range(len(buffer1)):
            assert self.client.read('*', 'test3')[i]['url'] == buffer0[i] and self.client.read('count', 'test3')[i][
                'count'] == buffer1[i]

    def test_size(self):
        info = self.client.mock_info()
        for i in range(len(info)):
            self.client.execute_query(fetch=True, query=f'insert into test4 (ip,code,size,url)'
                                                        f' values ("{info[i][0]}","{info[i][1]}","{info[i][2]}","{info[i][3]}")')

    def test_ip_count(self):
        info = self.client.ip_counting()
        buffer0 = []
        buffer1 = []
        for i in range(len(info[0])):
            info[1].append(info[2].count(info[0][i]))
            if info[1][i] > min(info[1]):
                buffer0.append(info[0][i])
                buffer1.append(info[1][i])
                self.client.execute_query(fetch=True, query=f'insert into test5 (ip,count)'
                                                            f' values ("{info[0][i]}","{info[1][i]}")')
        for i in range(len(buffer1)):
            assert self.client.read('*', 'test5')[i]['ip'] == buffer0[i] and str(self.client.read('*', 'test5')[i][
                                                                                     'count']) == str(buffer1[i])
