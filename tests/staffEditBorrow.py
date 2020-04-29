import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class staffEditBorrow(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "sindhurapailla@gmail.com"
       pwd1 = "Team@123"
       Borrow_Member_NUID = ""
       Borrow_Book_Name = ""
       Borrow_Author_Name = ""
       Borrow_Category_Name = ""

       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/home")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[2]/div/div/a').click()
       driver.get("https://myclm.herokuapp.com/staff-login/")
       elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
       elem.send_keys(email)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
       elem.send_keys(pwd1)
       elem.send_keys(Keys.RETURN)

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[3]/div/div/p/a').click()

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a').click()


       elem = driver.find_element_by_xpath('//*[@id="id_Borrow_Member_NUID"]')
       elem.send_keys(Borrow_Member_NUID)

       elem = driver.find_element_by_xpath('//*[@id="id_Borrow_Book_Name"]')
       elem.send_keys(Borrow_Book_Name)

       elem = driver.find_element_by_xpath('//*[@id="id_Borrow_Author_Name"]')
       elem.send_keys(Borrow_Author_Name)

       elem = driver.find_element_by_xpath('//*[@id="id_Borrow_Category_Name"]')
       elem.send_keys(Borrow_Category_Name)

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
       time.sleep(1)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
