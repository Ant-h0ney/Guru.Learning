from selene.support.shared import browser
from selene import be
from selenium.webdriver import Keys

browser.open('chrome://settings/')
browser.config.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')
browser.open('https://demoqa.com/automation-practice-form')
browser.config.hold_browser_open = True

browser.element('#firstName').should(be.blank).type('Anthony')
browser.element('#lastName').should(be.blank).type('Kononov')
browser.element('#userEmail').should(be.blank).type('mail@mail.ru')
browser.element('#gender-radio-3').parent_element.click()
browser.element('#userNumber').should(be.blank).type('1234567891')
browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
browser.element('#subjectsInput').click().type('Ma').press_enter().type('ch').press_enter()
browser.element('#hobbies-checkbox-2').parent_element.click()
browser.element('#currentAddress').should(be.blank).type('My real address will never appear here')
browser.element('#react-select-3-input').should(be.blank).type('u').press_enter()
browser.element('#react-select-4-input').should(be.blank).type('Luck').press_enter()
browser.element('#submit').click()