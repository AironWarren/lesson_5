import os
import allure
from demoqa_tests.Form_registration import RegistrationPage

from selene import browser, be, have

file = os.getcwd() + r'/ws/test/pictures/if-and-if-else.png'

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


@allure.tag('web')
@allure.label('owner', 'AironWarren')
@allure.story('User authorization')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_student_registration_form(open_browser):
    # removing ads

    registration_page = RegistrationPage()

    registration_page.removing_banners()

    # WHEN
    # the desired siteh
    registration_page.check_title('DEMOQA')

    # user initials
    registration_page.fill_first_name(student_registration_form['first_name'])
    registration_page.fill_last_name(student_registration_form['last_name'])
    registration_page.fill_email(student_registration_form['email'])

    # gender
    registration_page.choose_gender(student_registration_form['gender'])

    # userNumber
    registration_page.fill_phone_number(student_registration_form['phone_number'])

    # dateOfBirthInput
    registration_page.fill_in_the_date_of_birth(student_registration_form['date_of_birth']['month'],
                                                student_registration_form['date_of_birth']['year'],
                                                student_registration_form['date_of_birth']['day'])

    # subjects
    registration_page.fill_user_subjects(*student_registration_form['subjects'])

    # choosing a hobby
    registration_page.choose_hobby(student_registration_form['hobby'])

    # uploading an image
    registration_page.upload_picture(file)

    # sender's address
    registration_page.fill_current_Address(student_registration_form['address'])

    # scroll to the bottom of the page
    registration_page.scroll_to_the_end_of_the_page()

    # country and city selection
    registration_page.choose_state(student_registration_form['state'])
    registration_page.choose_city(student_registration_form['city'])

    # submit_the_form
    registration_page.submit_the_form()

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

    # registration_page.close_modal_contest()



