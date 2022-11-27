from api.base import ApiBase
import uuid
import pytest
from api.client import SegmentNotCreated, SegmentNotDeleted, CampaignNotCreated, CampaignNotDeleted


@pytest.mark.API
class TestApi(ApiBase):
    authorize = True

    def test_segment_vk(self):
        action = self.api_client.post_segment_vk(uuid.uuid4())
        if action[1] == 200:
            pass
        else:
            raise SegmentNotCreated
        if self.api_client.delete_segment(action[0]) == 204:
            pass
        else:
            raise SegmentNotDeleted

    def test_segment_games(self):
        action = self.api_client.post_segment_games(uuid.uuid4())
        if action[1] == 200:
            pass
        else:
            raise SegmentNotCreated
        if self.api_client.delete_segment(action[0]) == 204:
            pass
        else:
            raise SegmentNotDeleted

    def test_campaign(self):
        action = self.api_client.post_campaign(uuid.uuid4())
        print(action)
        if action[1] == 200:
            pass
        else:
            raise CampaignNotCreated
        if self.api_client.delete_campaign(action[0]) == 204:
            pass
        else:
            raise CampaignNotDeleted
