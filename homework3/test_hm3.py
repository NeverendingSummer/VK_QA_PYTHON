from api.base import ApiBase
import uuid
import pytest

# class TestSmnth(BaseCase):
#     authorize = True
#
#     def test_kek(self):
#         print("kewk")
#         self.groups_page.creating_groups()
#
#     def test_segment_creation(self):
#         """
#         Тест на создание аудиторного сегмента
#         """
#         segment_name = str(uuid.uuid4())
#         self.segment_page.create_segment(segment_name, timeout=5)
#         self.segment_page.success_check(segment_name, timeout=5)


class TestTwo(ApiBase):
    authorize = True
    #@pytest.mark.skip("skip")
    def test_segment(self):
        name = uuid.uuid4()
        self.api_client.post_segment_vk(name)
        self.api_client.delete_segment(name)


    def test_second(self):
        name = uuid.uuid4()
        self.api_client.create_segment_games(name)
        self.api_client.delete_segment(name)

