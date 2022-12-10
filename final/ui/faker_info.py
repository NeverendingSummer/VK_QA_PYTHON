import pytest
from faker import Faker
from random_username.generate import generate_username

fake = Faker()

def create_fake_info():
    name = fake.name().split(' ')
    email = fake.email()
    username = generate_username(1)[0]
    password = fake.password()
    return name[0], name[1], username, email, password

print(create_fake_info()[0]*2,create_fake_info()[1:])