import uuid
import pytest
from base import BaseCase


@pytest.mark.UI
class TestTwo(BaseCase):

    def test_create_campaign(self, file_path):
        campaing_name = str(uuid.uuid4())
        ad_url = "https://www.nestle.com/brands/chocolate-confectionery/kitkat"
        self.ad_page.create_ad_campaign(ad_url, timeout=15)
        self.ad_page.drop_video(file_path, timeout=15)
        self.ad_page.submit(campaing_name, timeout=15)
        self.ad_page.success_check(campaing_name, timeout=15)

    def test_segment_creation(self):
        segment_name = str(uuid.uuid4())
        self.segment_page.create_segment(segment_name, timeout=5)
        self.segment_page.success_check(segment_name, timeout=15)