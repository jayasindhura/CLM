import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class memberChangePassword(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "jpailla@unomaha.edu"
       pwd1 = "Team@123"
       old_pwd = "Team@123"
       new_pwd = "Team@123"
       new_pwd1 = "Team@123"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/home")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[1]/div/div/a').click()
       #elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[1]/div/div/p[1]/a').click()
       driver.get("https://myclm.herokuapp.com/member-login/")

       elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
       elem.send_keys(email)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
       elem.send_keys(pwd1)
       elem.send_keys(Keys.RETURN)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[3]/div/div/p/a').click()

       elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a').click()

       elem = driver.find_element_by_xpath('//*[@id="id_old_password"]')
       elem.send_keys(old_pwd)
       elem = driver.find_element_by_xpath('//*[@id="id_new_password1"]')
       elem.send_keys(new_pwd)
       elem = driver.find_element_by_xpath('//*[@id="id_new_password2"]')
       elem.send_keys(new_pwd1)
       elem = driver.find_element_by_xpath('//*[@id="content-main"]/form/div/div/input').click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
