import pytest

# from test_api.builder import Builder


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        # self.builder = Builder()

        if self.authorize:
            self.api_client.login()
