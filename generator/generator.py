import random

from data.data import Person

from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()

""" Генерация персональных данных """


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        mobile=faker_ru.msisdn(),
        current_address=faker_ru.address(),
    )
