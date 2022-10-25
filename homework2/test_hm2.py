import uuid
import pytest
from base import BaseCase
import allure


@allure.link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", name='Click me')
@pytest.mark.UI
class TestTwo(BaseCase):

    def test_create_campaign(self, file_path):
        """
        Тест на создание рекламной кампании, в качестве примера взят бренд KitKat
        """
        campaing_name = str(uuid.uuid4())
        ad_url = "https://www.nestle.com/brands/chocolate-confectionery/kitkat"
        self.ad_page.create_ad_campaign(ad_url, timeout=15)
        self.ad_page.drop_video(file_path, timeout=15)
        self.ad_page.submit(campaing_name, timeout=15)
        self.ad_page.success_check(campaing_name, timeout=15)

    def test_segment_creation(self):
        """
        Тест на создание аудиторного сегмента
        """
        segment_name = str(uuid.uuid4())
        self.segment_page.create_segment(segment_name, timeout=5)
        self.segment_page.success_check(segment_name, timeout=15)

    def test_group_creation(self):
        """
        Тест на создание сегмента с испочником данных VK образовние с типом "Группы OK и VK"
        """
        self.groups_page.creating_groups()