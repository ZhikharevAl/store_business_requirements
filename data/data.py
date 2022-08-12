from dataclasses import dataclass

"""" Создание класса данных Человека """


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    email: str = None
    mobile: str = None
    current_address: str = None