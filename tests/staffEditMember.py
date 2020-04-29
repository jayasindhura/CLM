import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class staffEditMember(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_website(self):
       email = "sindhurapailla@gmail.com"
       pwd1 = "Team@123"
       Member_NUID = ""
       First_Name = ""
       Middle_Name = ""
       Last_Name = ""
       Organization = ""
       Role = ""
       Email = ""
       Address = ""
       City = ""
       State = ""
       Zip_Code = ""
       Phone = ""
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

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div[1]/div/div/p/a').click()

       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a').click()


       elem = driver.find_element_by_xpath('//*[@id="id_Member_NUID"]')
       elem.send_keys(Member_NUID)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_first_name"]')
       elem.send_keys(First_Name)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_middle_name"]')
       elem.send_keys(Middle_Name)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_last_name"]')
       elem.send_keys(Last_Name)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_organization"]')
       elem.send_keys(Organization)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_role"]')
       elem.send_keys(Role)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_email"]')
       elem.send_keys(Email)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_address"]')
       elem.send_keys(Address)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_city"]')
       elem.send_keys(City)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_state"]')
       elem.send_keys(State)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_zipcode"]')
       elem.send_keys(Zip_Code)
       elem = driver.find_element_by_xpath('//*[@id="id_Member_phone"]')
       elem.send_keys(Phone)
       elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()

       time.sleep(1)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
