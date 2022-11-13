from api.base import ApiBase
import uuid
import pytest


@pytest.mark.API
class TestApi(ApiBase):
    authorize = True

    def test_segment_vk(self):
        name = uuid.uuid4()
        self.api_client.post_segment_vk(name)
        self.api_client.delete_segment(name)

    def test_segment_games(self):
        name = uuid.uuid4()
        self.api_client.post_segment_games(name)
        self.api_client.delete_segment(name)

    def test_campaign(self):
        name = uuid.uuid4()
        self.api_client.post_campaign(name)
        self.api_client.delete_campaign(name)
