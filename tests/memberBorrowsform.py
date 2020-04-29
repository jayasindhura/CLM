import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class memberBorrowsform(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "jpailla@unomaha.edu"
       pwd1 = "Team@123"
       Borrow_Member_NUID = "98659853"
       Borrow_Book_Name = "Sprint-How to Solve big problems"
       Borrow_Author_Name = "Tony R Stark"
       Borrow_Category_Name = "MIS"

       driver = self.driver
       driver.maximize_window()
       driver.get("http://myclm.herokuapp.com/home")
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div/div[1]/div/div/a').click()
       driver.get("https://myclm.herokuapp.com/member-login/")
       #time.sleep(1)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
       elem.send_keys(email)
       elem = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
       elem.send_keys(pwd1)
       elem.send_keys(Keys.RETURN)
       #time.sleep(1)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[3]/div/div/p/a').click()
       #time.sleep(1)



       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
       time.sleep(1)

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
