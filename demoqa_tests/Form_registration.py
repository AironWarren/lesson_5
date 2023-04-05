from selene import browser, be, have


class RegistrationPage:
    def __init__(self):
        self.information_from_the_drop_down_list = browser.all('[id^=react-select][id*=option]')

    def check_title(self, title):
        browser.should((have.title(title)))

    def removing_banners(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

    def fill_first_name(self, name):
        browser.element('#firstName').type(name)

    def fill_last_name(self, surname):
        browser.element('#lastName').type(surname)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)

    def fill_in_the_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        if int(day/10) != 0:
            browser.element(f'.react-datepicker__day--0{day}').click()
        else:
            browser.element(f'.react-datepicker__day--00{day}').click()

    def fill_user_subjects(self, *args):
        for subject in args:
            browser.element('#subjectsInput').type(subject)
            browser.all('.subjects-auto-complete__menu').element_by(have.exact_text(subject)).click()

    def choose_hobby(self, hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    def upload_picture(self, file):
        browser.element("#uploadPicture").send_keys(file)

    def fill_current_Address(self, address):
        browser.element('#currentAddress').type(address)

    def scroll_to_the_end_of_the_page(self):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def choose_state(self, state):
        browser.element('#state').click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(state)).click()

    def choose_city(self, city):
        browser.element('#city').click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(city)).click()

    def submit_the_form(self):
        browser.element('#submit').click()

    def check_name_modal_contest(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def assert_registered_user_info(self, first_name, last_name, email, gender, phone_number,
                                    date_of_birth, subjects, hobby, name_picture, address,
                                    state, city):

        str_subjects = ', '.join(subjects)

        if int(date_of_birth['day']/10) != 0:
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
        browser.element('#closeLargeModal').should(be.clickable).click()
