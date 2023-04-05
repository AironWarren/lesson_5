from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    mathematics = 'Maths'
    english = 'English'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: str
    subjects: List[Subject]
    hobby: Hobby
    address: str
    name_picture: str
    state: str
    city: str
