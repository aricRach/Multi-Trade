from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import os  # in order to upload file


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            r"C:\Users\aric\Desktop\מדעי המחשב\שנה ג\פרויקט גמר\chromedriver.exe")
        self.browser.get('http://127.0.0.1:5000/')

    # def test_login_fail(self):
    #
    #     self.browser.find_element_by_link_text("login").click()
    #     self.email_field = self.browser.find_element_by_name('email')  # Find the email box
    #     self.email_field.send_keys('EmailNotExist@gmail.com')
    #     self.pass_field = self.browser.find_element_by_name('pass')
    #     self.pass_field.send_keys('123123')
    #
    #     self.isChecked = self.browser.find_element_by_id("remember me").click()
    #     self.button=self.browser.find_element_by_id("submit").click()
    #     assert(self.browser.current_url != 'http://127.0.0.1:5000/')

    def test_login_succeed(self):
        self.browser.find_element_by_link_text("login").click()
        self.email_field = self.browser.find_element_by_name(
            'email')  # Find the email box
        self.email_field.send_keys('yosi@gmail.com')
        self.pass_field = self.browser.find_element_by_name('pass')
        self.pass_field.send_keys('123123')

        self.isChecked = self.browser.find_element_by_id("remember me").click()
        self.button = self.browser.find_element_by_id("submit").click()
        assert(self.browser.current_url == 'http://127.0.0.1:5000/')

        # add item
        self.openNavBar = self.browser.find_element_by_id(
            'navbarDropdown').click()
        self.browser.find_element_by_link_text("my collection").click()

        self.addIteme = self.browser.find_element_by_id('add item').click()
        time.sleep(2)
        self.itemName_field = self.browser.find_element_by_id('input name')
#        self.itemName_field.send_keys("test item")
        self.itemDetails_field = self.browser.find_element_by_name(
            'itemDetails')
#        self.itemDetails_field.send_keys('brand new item')
        time.sleep(2)
        self.browser.find_element_by_id("image").send_keys(
            os.getcwd() + "/example.jpg")
        time.sleep(2)
        self.submit_field = self.browser.find_element_by_id("submit").click()
        time.sleep(2)
        assert(self.browser.current_url == 'http://127.0.0.1:5000/collection/')

        # we need to do :
        # edit item
        # delete item

        # logout
        self.browser.find_element_by_link_text("logOut").click()
        assert(self.browser.current_url == 'http://127.0.0.1:5000/')
        time.sleep(2)


    #
    # def test_registration_succeed(self):
    #     self.browser.find_element_by_link_text("sign up").click()
    #     self.email_field = self.browser.find_element_by_name('email')  # Find the email box
    #     self.email_field.send_keys('testUser1@gmail.com')
    #
    #     self.firstName_field = self.browser.find_element_by_name('fn')  # Find the email box
    #     self.firstName_field.send_keys('test')
    #
    #     self.lastName_field = self.browser.find_element_by_name('ln')  # Find the email box
    #     self.lastName_field.send_keys('user')
    #
    #     self.pass_field = self.browser.find_element_by_name('pass')
    #     self.pass_field.send_keys('Secret')
    #
    #     self.passConfirm_field = self.browser.find_element_by_name('confirmPass')
    #     self.passConfirm_field.send_keys('Secret')
    #
    #     self.state_field = self.browser.find_element_by_id('myInput') # ******** ID
    #     self.state_field.send_keys('J')
    #     self.state_field.send_keys(Keys.DOWN)
    #     self.state_field.send_keys(Keys.ENTER)
    #
    #     self.phonePrefix_field = self.browser.find_element_by_name('phone1Prefix')
    #     self.phonePrefix_field.send_keys('054')
    #
    #     self.phoneNum_field = self.browser.find_element_by_name('phoneNum')
    #     self.phoneNum_field.send_keys('5624958')
    #
    #     self.isChecked = self.browser.find_element_by_id("remember me").click()
    #
    #     self.submit_field = self.browser.find_element_by_id("submit").click()
    #     assert(self.browser.current_url == 'http://127.0.0.1:5000/')
    #
    # def test_presonal_details(self):
    #         self.browser.find_element_by_link_text("login").click()
    #         self.email_field = self.browser.find_element_by_name('email')  # Find the email box
    #         self.email_field.send_keys('yosi@gmail.com')
    #         self.pass_field = self.browser.find_element_by_name('pass')
    #         self.pass_field.send_keys('123123')
    #
    #         self.isChecked = self.browser.find_element_by_id("remember me").click()
    #         self.button=self.browser.find_element_by_id("submit").click()
    #         assert(self.browser.current_url == 'http://127.0.0.1:5000/')
    #         self.openNavBar = self.browser.find_element_by_id('navbarDropdown').click()
    #         self.browser.find_element_by_link_text("personal details").click()
    #
    #         self.state_field = self.browser.find_element_by_id('myInput')
    #         self.state_field.clear()
    #         self.state_field.send_keys('H')
    #         self.state_field.send_keys(Keys.DOWN)
    #         self.state_field.send_keys(Keys.ENTER)
    #
    #         self.phonePrefix_field = self.browser.find_element_by_name('phone1Prefix')
    #         self.phonePrefix_field.send_keys('055')
    #
    #         self.phoneNum_field = self.browser.find_element_by_name('phoneNum')
    #         self.phoneNum_field.clear()
    #         self.phoneNum_field.send_keys('1234567')
    #
    #         self.submit_field = self.browser.find_element_by_id("submit").click()
    #         assert(self.browser.current_url == 'http://127.0.0.1:5000/')
if __name__ == '__main__':

    unittest.main()
