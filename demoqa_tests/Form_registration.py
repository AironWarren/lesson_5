from selene import browser, be, have
import enum

from users.user import User


class Hobby(enum.Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Gender(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName').should(be.blank)
        self.last_name = browser.element('#lastName').should(be.blank)
        self.email = browser.element('#userEmail').should(be.blank)
        self.gender = browser.all('[name=gender]')
        self.number = browser.element('#userNumber').should(be.blank)

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')

        self.subjects_input = browser.element('#subjectsInput').should(be.blank)
        self.item_from_the_menu = browser.all('.subjects-auto-complete__menu')

        self.hobby = browser.all('[for^=hobbies-checkbox]')

        self.upload_picture = browser.element("#uploadPicture")
        self.current_address = browser.element('#currentAddress').should(be.blank)

        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.information_from_the_drop_down_list = browser.all('[id^=react-select][id*=option]')

        self.submit_the_form = browser.element('#submit')

        self.check_modal_title = browser.element('#example-modal-sizes-title-lg')
        self.close_modal = browser.element('#closeLargeModal').should(be.clickable)

    def check_title(self, title):
        browser.should((have.title(title)))

    def removing_banners(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

    def fill_first_name(self, name):
        self.first_name.type(name)

    def fill_last_name(self, surname):
        self.last_name.type(surname)

    def fill_email(self, email):
        self.email.type(email)

    def choose_gender(self, gender):
        self.gender.element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, phone_number):
        self.number.type(phone_number)

    def fill_in_the_date_of_birth(self, date_of_birth):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(str(date_of_birth.month))
        self.date_of_birth_year.type(str(date_of_birth.year))

        if int(date_of_birth.day / 10) != 0:
            browser.element(f'.react-datepicker__day--0{date_of_birth.day}').click()
        else:
            browser.element(f'.react-datepicker__day--00{date_of_birth.day}').click()

    def fill_user_subjects(self, *args):
        for subject in args:
            self.subjects_input.type(subject)
            self.item_from_the_menu.element_by(have.exact_text(subject)).click()

    def choose_hobby(self, hobby):
        self.hobby.element_by(have.text(hobby)).click()

    def upload_picture(self, file):
        self.upload_picture.send_keys(file)

    def fill_current_Address(self, address):
        self.current_address.type(address)

    def scroll_to_the_end_of_the_page(self):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def choose_state(self, state):
        self.state.click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(state)).click()

    def choose_city(self, city):
        self.city.click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(city)).click()

    def submit_the_form(self):
        self.submit_the_form.click()

    def check_name_modal_contest(self):
        self.check_modal_title.should(have.text('Thanks for submitting the form'))

    def assert_registered_user_info(self, first_name, last_name, email, gender, phone_number,
                                    date_of_birth, subjects, hobby, name_picture, address,
                                    state, city):

        str_subjects = ', '.join(subjects)

        if int(date_of_birth['day'] / 10) != 0:
            date_of_birth['day'] = 'date_of_birth["day"]}'
        else:
            date_of_birth['day'] = f'0{date_of_birth["day"]}'

        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{first_name} {last_name}',
                email,
                gender,
                phone_number,
                f'{date_of_birth["day"]} {date_of_birth["month"]},{date_of_birth["year"]}',
                str_subjects,
                hobby,
                name_picture,
                address,
                f'{state} {city}',
            )
        )

    def close_modal_contest(self):
        self.close_modal.click()

    def registration_form(self, student: User):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.choose_gender(student.gender)
        self.fill_phone_number(student.phone_number)
        self.fill_in_the_date_of_birth(student.date_of_birth)
        self.fill_user_subjects(student.subjects)
        self.choose_hobby(student.hobby)
        self.upload_picture(student.name_picture)
        self.fill_current_Address(student.address)
        self.choose_state(student.state)
        self.choose_city(student.city)
