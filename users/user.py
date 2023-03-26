from dataclasses import dataclass
from datetime import date
from enum import Enum


class HobbyAndGender(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'

    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: HobbyAndGender
    phone_number: str
    date_of_birth: date
    subjects: list
    hobby: HobbyAndGender
    address: str
    name_picture: str
    state: str
    city: str
