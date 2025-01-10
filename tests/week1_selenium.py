from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from unittest import TestCase, main
from time import sleep


class eis_test(TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_demo(self):
		browser = self.browser
		browser.get("http://demo.guru99.com/test/login.html")
		email = browser.find_element(By.ID, 'email')
		email.clear()
		email.send_keys("test@test.test")
		password = browser.find_element(By.ID, 'passwd')
		password.clear()
		password.send_keys("test")
		submitButton = browser.find_element(By.ID, 'SubmitLogin')
		submitButton.send_keys(Keys.ENTER)
		sleep(2)
		success = browser.find_element(By.CSS_SELECTOR, 'h3')
		self.assertIn('Successfully Logged in...', success.text)

	def test_tabs(self):
		browser = self.browser
		browser.get("about:blank")
		sleep(2)
		browser.execute_script("window.open('');")
		browser.switch_to.window(browser.window_handles[1])
		sleep(2)
		browser.execute_script("window.open('');")
		browser.switch_to.window(browser.window_handles[2])
		sleep(2)
		browser.switch_to.window(browser.window_handles[0])
		sleep(2)
		browser.close()

	def test_load(self):
		browser = self.browser
		browser.get("https://campusvirtualunillanos.co/login/index.php")
		fname = browser.find_element(By.ID, 'username')
		fname.clear()
		fname.send_keys('160003810')
		lname = browser.find_element(By.ID, 'password')
		lname.clear()
		lname.send_keys('Otakukran1004')
		submitButton = browser.find_element(By.ID, 'loginbtn')
		submitButton.send_keys(Keys.ENTER)
		sleep(5)
		courses = browser.find_elements(By.CLASS_NAME, 'coursename')
		print(f"The number of courses is {len(courses)}")
		course = browser.find_element(By.LINK_TEXT, 'CALIDAD DEL SOFTWARE: VERIFICACION Y VALIDACION')
		hover = ActionChains(browser).move_to_element(course).click()
		hover.perform()
		sleep(5)
		to_students = browser.find_element(By.LINK_TEXT, 'Participantes')
		hover = ActionChains(browser).move_to_element(to_students).click()
		hover.perform()
		sleep(5)
		students = browser.find_elements(By.CSS_SELECTOR, 'tr:not(.emptyrow)')
		print(f"The number of students is {len(students)-1}")
		self.assertGreater(len(students), 0)

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	main()