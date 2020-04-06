import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class staffForgotPassword(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "jpailla@unomaha.edu"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/home/")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[2]/div/div/p[3]/a').click()
       time.sleep(2)
       driver.get("https://myclm.herokuapp.com/accounts/password_reset/")
       elem = driver.find_element_by_xpath('//*[@id="id_email"]')
       elem.send_keys(email)
       elem.send_keys(Keys.RETURN)
       #elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div / div / form / div[4] / button').click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
