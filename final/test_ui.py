import pytest
from faker import Faker
from random_username.generate import generate_username

from ui.base import BaseCase

fake = Faker()


class TestTwo(BaseCase):
    authorize = False
    name = fake.name().split(' ')

    @pytest.mark.parametrize("name,surname,username,email,password",
                             [(f'{name[0]}', f'{name[1]}', f'{generate_username(1)[0]}',
                               f'{fake.email()}',
                               f'{fake.password()}')
                                 , (f'{name[0]}', f'{name[1]}', f'{generate_username(1)[0]}',
                                    f'{fake.email()}',
                                    f'{fake.password()}')])
    def test_registry(self, name, surname, username, email, password):
        self.registry_page.insert_values(name, surname, username, email, password)
        assert self.registry_page.check_registration() == username
