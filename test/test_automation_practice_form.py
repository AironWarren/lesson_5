import datetime
import os

from demoqa_tests.Form_registration import RegistrationPage, Gender, Hobby
from users.user import User

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

student = User(first_name='Slava', last_name='Komesarenko', email='Kslavon345@gmail.ru', gender=Gender.female,
               phone_number='9138761122', date_of_birth=datetime.date(2007, 12, 2), subjects=['Maths', 'English'],
               hobby=Hobby.music, address="Moskovskaya street 15", name_picture='if-and-if-else.png', state='Haryana',
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

    registration_page.assert_registered_user_info(student_registration_form['first_name'],
                                                  student_registration_form['last_name'],
                                                  student_registration_form['email'],
                                                  student_registration_form['gender'],
                                                  student_registration_form['phone_number'],
                                                  student_registration_form['date_of_birth'],
                                                  student_registration_form['subjects'],
                                                  student_registration_form['hobby'],
                                                  student_registration_form['name_picture'],
                                                  student_registration_form['address'],
                                                  student_registration_form['state'],
                                                  student_registration_form['city']
                                                  )

    registration_page.close_modal_contest()
