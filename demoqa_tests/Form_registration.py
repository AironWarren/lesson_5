from selene import browser, be, have
from users.user import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.number = browser.element('#userNumber')

        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')

        self.subjects_input = browser.element('#subjectsInput')
        self.item_from_the_menu = browser.all('.subjects-auto-complete__menu')

        self.hobby = browser.all('[for^=hobbies-checkbox]')

        self.picture = browser.element("#uploadPicture")
        self.current_address = browser.element('#currentAddress')

        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.information_from_the_drop_down_list = browser.all('[id^=react-select][id*=option]')

        self.submit = browser.element('#submit')


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
        date_of_birth = date_of_birth.split()
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(date_of_birth[1])
        self.date_of_birth_year.type(date_of_birth[2])
        browser.element(f'.react-datepicker__day--0{date_of_birth[0]}').click()

    def fill_user_subjects(self, subjects):
        for subject in subjects:
            self.subjects_input.type(subject)
            self.item_from_the_menu.element_by(have.exact_text(subject)).click()

    def choose_hobby(self, hobby):
        self.hobby.element_by(have.text(hobby)).click()

    def upload_picture(self, file):
        self.picture.send_keys(file)

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
        self.submit.click()

    def check_name_modal_contest(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def assert_registered_user_info(self, student: User):
        str_subjects = ', '.join(student.subjects)
        date_of_birth = student.date_of_birth.split()
        name_picture = (student.name_picture.split('\\'))[-1]

        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender,
                student.phone_number,
                f'{date_of_birth[0]} {date_of_birth[1]},{date_of_birth[2]}',
                str_subjects,
                student.hobby,
                name_picture,
                student.address,
                f'{student.state} {student.city}',
            )
        )

    def close_modal_contest(self):
        browser.element('#closeLargeModal').should(be.clickable).click()

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
        self.submit_the_form()
