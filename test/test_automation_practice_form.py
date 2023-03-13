from selene import browser, have, be
import os

from selenium.webdriver import ActionChains, Keys

NAME = "Slava"
SURNAME = "Ko"
EMAIL = "Kslavon345@gmail.ru"
NUMBER = "9138761122"


def test_form(open_browser):
    actions = ActionChains(browser.driver)

    file = os.getcwd() + r'\pictures\if-and-if-else.png'

    # removing unnecessary banners
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    # filling out the form
    browser.should((have.title('DEMOQA')))

    # first name
    browser.element('#firstName').should(be.blank).type(NAME)

    # last name
    browser.element('#lastName').should(be.blank).type(SURNAME)

    # email
    browser.element('#userEmail').should(be.blank).type(EMAIL)

    # gender
    browser.element('[for="gender-radio-2"]').should(have.text('Female')).click()

    # mobile number
    browser.element('#userNumber').should(be.blank).type(NUMBER)

    '''
    Немного костыльная проверка и я не уверен что она вообще работает, но значение меняется, но если потом кликнуть
    вернется default значение, печально
    '''
    # browser.element('#dateOfBirthInput').click()
    # browser.execute_script("document.querySelector('#dateOfBirthInput').value = '02 Dec 2007'")
    # browser.element('#dateOfBirthInput').should(have.value('02 Dec 2007')).click()

    '''
    Второй вариант как мне кажется правильный
    '''
    # В CSS точка перед названием селектора означает, что это селектора класса
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="11"]').should(have.text('December')).click()
    browser.element('.react-datepicker__year-select option[value="2007"]').click()
    browser.element('.react-datepicker__day--002').should(have.text('2')).click()

    # subjects
    browser.element('#subjectsInput').should(be.blank).type('Maths')
    browser.all('.subjects-auto-complete__menu').element_by(have.exact_text('Maths')).click()
    browser.element('#subjectsInput').should(be.blank).type('English')
    browser.all('.subjects-auto-complete__menu-list').element_by(have.exact_text('English')).click()

    # hobbies
    browser.element('[for="hobbies-checkbox-3"]').should(have.text('Music')).click()

    # picture
    browser.element("input[type=file]").send_keys(file)

    # Address
    browser.element('#currentAddress').should(be.blank).type("Russia")

    # scroll down to the bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # state and city
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').should(have.text('Haryana')).click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.text('Karnal')).click()

    # submitting a form
    browser.element('#submit').click()

    # checking the completed form
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').element_by_its('td', have.text('Student Name')).all('td')[1].should(
        have.text(f'{NAME} {SURNAME}'))
    browser.all('tr').element_by_its('td', have.text('Student Email')).all('td')[1].should(have.text(EMAIL))
    browser.all('tr').element_by_its('td', have.text('Gender')).all('td')[1].should(have.text('Female'))
    browser.all('tr').element_by_its('td', have.text('Mobile')).all('td')[1].should(have.text(NUMBER))
    browser.all('tr').element_by_its('td', have.text('Date of Birth')).all('td')[1].should(
        have.text('02 December,2007'))
    browser.all('tr').element_by_its('td', have.text('Subjects')).all('td')[1].should(have.text('Maths, English'))
    browser.all('tr').element_by_its('td', have.text('Hobbies')).all('td')[1].should(have.text('Music'))
    browser.all('tr').element_by_its('td', have.text('Picture')).all('td')[1].should(have.text('if-and-if-else.png'))
    browser.all('tr').element_by_its('td', have.text('Address')).all('td')[1].should(have.text('Russia'))
    browser.all('tr').element_by_its('td', have.text('State and City')).all('td')[1].should(have.text('Haryana Karnal'))

    browser.element('#closeLargeModal').should(be.clickable).click()
