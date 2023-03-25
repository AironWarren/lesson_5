from selene import browser, have, be
import os

from selenium.webdriver import ActionChains, Keys

NAME = "Slava"
SURNAME = "Komesarenko"
EMAIL = "Kslavon345@gmail.ru"
NUMBER = "9138761122"
file = os.getcwd() + r'\pictures\if-and-if-else.png'


def test_form(open_browser):
    # removing ads
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    # WHEN
    # the desired site
    browser.should((have.title('DEMOQA')))

    # user initials
    browser.element('#firstName').should(be.blank).type(NAME)
    browser.element('#lastName').should(be.blank).type(SURNAME)
    browser.element('#userEmail').should(be.blank).type(EMAIL)

    # # gender
    browser.element('[name=gender][value=Female]+label').click()

    # userNumber
    browser.element('#userNumber').should(be.blank).type(NUMBER)

    # dateOfBirthInput
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('December')
    browser.element('.react-datepicker__year-select').type('2007')
    browser.element(f'.react-datepicker__day--00{2}').click()

    # subjects
    browser.element('#subjectsInput').should(be.blank).type('Maths')
    browser.all('.subjects-auto-complete__menu').element_by(have.exact_text('Maths')).click()
    browser.element('#subjectsInput').should(be.blank).type('English')
    browser.all('.subjects-auto-complete__menu').element_by(have.exact_text('English')).click()

    # choosing a hobby
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()

    # uploading an image
    browser.element("#uploadPicture").send_keys(file)

    # sender's address
    browser.element('#currentAddress').should(be.blank).type("Moskovskaya street 15")

    # scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # country and city selection
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').click()

    # THEN
    # checking the completed form
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Slava Komesarenko',
            'Kslavon345@gmail.ru',
            'Female',
            '9138761122',
            '02 December,2007',
            'Maths, English',
            'Music',
            'if-and-if-else.png',
            'Moskovskaya street 15',
            'Haryana Karnal',
        )
    )

    browser.element('#closeLargeModal').should(be.clickable).click()
