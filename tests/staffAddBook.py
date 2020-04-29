import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class staffAddBook(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "sindhurapailla@gmail.com"
       pwd1 = "Team@123"
       Book_Title = "Sprint-How to Solve big problems"
       Book_ISBN = "978-1-133-62965-8"
       Book_publisher ="Goodreads"
       Book_author_name = "Tony R Stark"
       Book_category_name = "MIS"

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
       
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[2]/div/div/p/a').click()
       
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
       

       elem = driver.find_element_by_xpath('//*[@id="id_Book_Title"]')
       elem.send_keys(Book_Title)
       elem = driver.find_element_by_xpath('//*[@id="id_Book_ISBN"]')
       elem.send_keys(Book_ISBN)
       elem = driver.find_element_by_xpath('//*[@id="id_Book_publisher"]')
       elem.send_keys(Book_publisher)
       
       elem = driver.find_element_by_xpath('//*[@id="id_Book_author_name"]')
       elem.send_keys(Book_author_name)
       
       elem = driver.find_element_by_xpath('//*[@id="id_Book_category_name"]')
       elem.send_keys(Book_category_name)
       
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
       




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
