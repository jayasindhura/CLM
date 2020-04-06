import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class memberSignup(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "sindhura1234@unomaha.edu"
       pwd1 = "Team@123"
       pwd2 = "Team@123"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[1]/div/div/p[1]/a').click()
       driver.get("https://myclm.herokuapp.com/member-signup/")
       time.sleep(2)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
       elem.send_keys(email)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
       elem.send_keys(pwd1)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword2"]')
       elem.send_keys(pwd2)
       elem.send_keys(Keys.RETURN)
       #elem = driver.find_element_by_xpath('// *[ @ id = "app-layout"] / div / div / div / div / div / form / div[4] / button').click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
