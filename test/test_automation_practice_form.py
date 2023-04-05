import datetime
import os

from demoqa_tests.Form_registration import RegistrationPage
from users.user import User, Hobby, Gender, Subject

file = os.getcwd() + r'\pictures\if-and-if-else.png'

student_registration_form = {
    'first_name': 'Slava',
    'last_name': 'Komesarenko',
    'email': 'Kslavon345@gmail.ru',
    'gender': 'Female',
    'phone_number': '9138761122',
    'date_of_birth': {
        'month': 'December',
        'year': '2007',
        'day': 2
    },
    'subjects': ['Maths', 'English'],
    'hobby': 'Music',
    'address': "Moskovskaya street 15",
    'name_picture': 'if-and-if-else.png',
    'state': 'Haryana',
    'city': 'Karnal'
}

student = User(first_name='Slava', last_name='Komesarenko', email='Kslavon345@gmail.ru',
               gender=Gender.female.value,
               phone_number='9138761122', date_of_birth=datetime.date(2007, 12, 2).strftime("%d %B %Y"),
               subjects=[Subject.mathematics.value, Subject.english.value],
               hobby=Hobby.music.value, address="Moskovskaya street 15", name_picture=file,
               state='Haryana',
               city='Karnal')


def test_student_registration_form(open_browser):
    # removing ads
    registration_page = RegistrationPage()

    registration_page.removing_banners()

    # WHEN
    registration_page.registration_form(student)
    # THEN
    # checking the completed form
    registration_page.check_name_modal_contest()

    registration_page.assert_registered_user_info(student)

    registration_page.close_modal_contest()
