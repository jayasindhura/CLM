import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class staffSignup(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "jayapailla16@unomaha.edu"
       pwd1 = "Team@123"
       pwd2 = "Team@123"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/home/")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[2]/div/div/p[2]/a').click()

       driver.get("https://myclm.herokuapp.com/staff-signup/")
       #time.sleep(1)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
       elem.send_keys(email)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
       elem.send_keys(pwd1)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword2"]')
       elem.send_keys(pwd2)
       elem.send_keys(Keys.RETURN)
       #elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div / div / form / div[4] / button').click()
       #time.sleep(1)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
