import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class adminLogout(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "groyce@unomaha.edu"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(email)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       #driver.get("http://myclm.herokuapp.com/admin")
       elem = driver.find_element_by_xpath('//*[@ id = "user-tools"]/a[3]').click()
       assert "Logged Out"
       time.sleep(1)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
