import enum
from dataclasses import dataclass
from datetime import date
from demoqa_tests.Form_registration import Gender, Hobby


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: date
    subjects: list
    hobby: Hobby
    address: str
    name_picture: str
    state: str
    city: str
