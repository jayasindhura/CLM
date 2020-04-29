import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests import MemberSignup,adminlogin,memberForgotPassword,staffAddBook,staffEditMember,StaffSignup,memberLogin,staffAddMember,staffForgotPassword,memberBooks,memberLogout,staffChangePassword,staffLogin,memberBorrowsEdit,membersChangePassword,staffEditBook,staffLogout,adminLogout,memberBorrowsform,membersList,staffEditBorrow,staffNewBorrow,Borrowsummarypdf
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(unittest.loader.findTestCases(adminlogin))

suite.addTest(unittest.loader.findTestCases(StaffSignup))
suite.addTest(unittest.loader.findTestCases(staffForgotPassword))
suite.addTest(unittest.loader.findTestCases(staffLogin))
suite.addTest(unittest.loader.findTestCases(staffAddMember))
suite.addTest(unittest.loader.findTestCases(staffEditMember))
suite.addTest(unittest.loader.findTestCases(staffAddBook))
suite.addTest(unittest.loader.findTestCases(staffEditBook))
suite.addTest(unittest.loader.findTestCases(staffNewBorrow))
suite.addTest(unittest.loader.findTestCases(staffEditBorrow))
suite.addTest(unittest.loader.findTestCases(staffChangePassword))
suite.addTest(unittest.loader.findTestCases(staffLogout))
suite.addTest(unittest.loader.findTestCases(Borrowsummarypdf))
suite.addTest(unittest.loader.findTestCases(MemberSignup))
suite.addTest(unittest.loader.findTestCases(memberLogin))
suite.addTest(unittest.loader.findTestCases(membersList))
suite.addTest(unittest.loader.findTestCases(memberBooks))
suite.addTest(unittest.loader.findTestCases(memberBorrowsform))
suite.addTest(unittest.loader.findTestCases(memberBorrowsEdit))
#suite.addTest(unittest.loader.findTestCases(membersChangePassword))
#suite.addTest(unittest.loader.findTestCases(memberForgotPassword))
suite.addTest(unittest.loader.findTestCases(memberLogout))

runner = unittest.TextTestRunner(verbosity=3)

result = runner.run(suite)

