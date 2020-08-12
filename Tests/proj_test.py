from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome(
    r"C:\Users\aric\Desktop\מדעי המחשב\שנה ג\פרויקט גמר\chromedriver.exe")
browser.get('http://127.0.0.1:5000/')


browser.find_element_by_link_text("login").click()
email_field = browser.find_element_by_name('email')  # Find the email box
email_field.send_keys('EmailNotExist@gmail.com')
pass_field = browser.find_element_by_name('pass')
pass_field.send_keys('123123')

isChecked = browser.find_element_by_id("remember me").click()

button = browser.find_element_by_id("submit").click()


assert (browser.current_url != 'http://127.0.0.1:5000/')

# openNavBar = browser.find_element_by_id('navbarDropdown').click()
# browser.find_element_by_link_text("personal details").click()
time.sleep(2)
browser.quit()


# browser.find_element_by_link_text("sign up").click()
# email_field = browser.find_element_by_name('email')  # Find the email box
# email_field.send_keys('testUser@gmail.com')
#
# firstName_field = browser.find_element_by_name('fn')  # Find the email box
# firstName_field.send_keys('test')
#
# lastName_field = browser.find_element_by_name('ln')  # Find the email box
# lastName_field.send_keys('user')
#
# pass_field = browser.find_element_by_name('pass')
# pass_field.send_keys('Secret')
#
# passConfirm_field = browser.find_element_by_name('confirmPass')
# passConfirm_field.send_keys('Secret')
#
# state_field = browser.find_element_by_id('myInput') # ******** ID
# state_field.send_keys('J')
# state_field.send_keys(Keys.DOWN)
# state_field.send_keys(Keys.ENTER)
#
# phonePrefix_field = browser.find_element_by_name('phone1Prefix')
# phonePrefix_field.send_keys('054')
#
# phoneNum_field = browser.find_element_by_name('phoneNum')
# phoneNum_field.send_keys('5624958')
#
# isChecked = browser.find_element_by_id("remember me").click()
#
# submit_field = browser.find_element_by_id("submit").click()
