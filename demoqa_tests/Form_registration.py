import allure
from selene import browser, be, have

from conftest import open_browser


class RegistrationPage:
    def __init__(self):
        # self.browser = open_browser
        self.information_from_the_drop_down_list = browser.all('[id^=react-select][id*=option]')

    @allure.step('Checking the page name')
    def check_title(self, title):
        browser.should((have.title(title)))

    @allure.step('Removing banners')
    def removing_banners(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

    @allure.step('Fill in firstName')
    def fill_first_name(self, name):
        browser.element('#firstName').should(be.blank).type(name)

    @allure.step('Fill in lastName')
    def fill_last_name(self, surname):
        browser.element('#lastName').should(be.blank).type(surname)

    @allure.step('Fill in userEmail')
    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    @allure.step('Fill in gender')
    def choose_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    @allure.step('Fill in userNumber')
    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').should(be.blank).type(phone_number)

    @allure.step('Choosing the date of birth')
    def fill_in_the_date_of_birth(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        if int(day/10) != 0:
            browser.element(f'.react-datepicker__day--0{day}').click()
        else:
            browser.element(f'.react-datepicker__day--00{day}').click()

    @allure.step('Fill in user subjects')
    def fill_user_subjects(self, *args):
        for subject in args:
            browser.element('#subjectsInput').should(be.blank).type(subject)
            browser.all('.subjects-auto-complete__menu').element_by(have.exact_text(subject)).click()

    @allure.step('Choosing the hobby')
    def choose_hobby(self, hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()

    @allure.step('Uploading a picture')
    def upload_picture(self, file):
        browser.element("#uploadPicture").send_keys(file)

    @allure.step('Fill in currentAddress')
    def fill_current_Address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    @allure.step('Moving down the window')
    def scroll_to_the_end_of_the_page(self):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Choosing the state')
    def choose_state(self, state):
        browser.element('#state').click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(state)).click()

    @allure.step('Choosing the city')
    def choose_city(self, city):
        browser.element('#city').click()
        self.information_from_the_drop_down_list.element_by(have.exact_text(city)).click()

    @allure.step('Sending the form')
    def submit_the_form(self):
        browser.element('#submit').click()

    @allure.step('Checking name modal contest')
    def check_name_modal_contest(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    @allure.step('Checking the correctness of the completed form')
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

    @allure.step('Closing modal contest')
    def close_modal_contest(self):
        browser.element('#closeLargeModal').should(be.clickable).click()
