import pytest
import pymysql
from sql import MysqlClient


class Start:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client: MysqlClient = mysql_client

class hm6(Start):
    pass