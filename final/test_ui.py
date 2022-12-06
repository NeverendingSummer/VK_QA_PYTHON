from ui.pages import main_page
from ui.base import BaseCase


class TestOne(BaseCase):

    def test_testa(self):
        self.driver.get('http://172.17.0.3:8080/')