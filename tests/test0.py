from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from unittest import TestCase, main
from time import sleep

class eis_test(TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_lol(self):
		urlGeneral = 'https://www.leagueoflegends.com/en-us/'
		urls = ['champions', 'news/tags/patch-notes', 'news/community/join-the-community']

		for url in urls:
			print("Resultado -> %s" % url)
			print("%s%s" % (urlGeneral, url))
			self.browser.get("%s%s" % (urlGeneral, url))
			sleep(3)
			logoList = self.browser.find_elements(By.CLASS_NAME, 'riotbar-footer-logo')
			res = []
			for logo in logoList:
				res.append(logo.text)
			self.assertEqual(len(res), 1, msg='Fallo en el resultado de -> %s' % (url))

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
		name = browser.find_element(By.ID, 'page-header')
		self.assertIn('RODRIGO ANDRÉS', name.text)
		pfp = browser.find_element(By.ID, 'user-menu-toggle')
		res = browser.find_element(By.LINK_TEXT, 'Cerrar sesión')
		hover = ActionChains(browser).move_to_element(pfp).move_to_element(res).click()
		hover.perform()
		sleep(5)
		url = browser.current_url
		self.assertEqual('https://campusvirtualunillanos.co/', url)

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	main()