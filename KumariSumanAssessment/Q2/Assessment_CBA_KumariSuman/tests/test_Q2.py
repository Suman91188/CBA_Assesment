"""# Q2
## Problem Description
Create a selenium script in java with test cases covering different values for Home Loan repayment
and validate the total loan repayment and total interest repayment.
You can access https://www.commbank.com.au and
then click on "Home Loan repayment calculator" to identify the online calculator.

## Response Requirements
- Source code and execution outcome (screen record) are both required from your GitHub
- Code needs to be successfully compiled and execution verified in JDK 1.8.0_265+, selenium 3.141+ and include all referenced jar's
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import time
import pytest
from pages.calculator import calculator
class TestCalculator():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.commbank.com.au")
        time.sleep(3)
        yield
        driver.close()

    """Running test Keeping productid constant and changing repayment type"""
    """Repayment type  = Principal and interest """
    def test_calculateHomeLoan(self,test_setup):
        print("Repayment type  = Principal and interest")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(0)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$11,417")
        cal.verifyTotalInterestRepayment("$1,417")


    def test_calculateHomeLoan1(self,test_setup):
        print("Repayment type  =Interest only 1 year")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(1)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$11,596")
        cal.verifyTotalInterestRepayment("$1,596")

    def test_calculateHomeLoan2(self,test_setup):
        print("Repayment type  =Interest only 2 year")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(2)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$11,776")
        cal.verifyTotalInterestRepayment("$1,776")

    def test_calculateHomeLoan3(self,test_setup):
        print("Repayment type  =Interest only 3 year")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(3)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$11,958")
        cal.verifyTotalInterestRepayment("$1,958")

    def test_calculateHomeLoan4(self,test_setup):
        print("Repayment type  =Interest only 4 year")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(4)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$12,140")
        cal.verifyTotalInterestRepayment("$2,140")

    def test_calculateHomeLoan5(self,test_setup):
        print("Repayment type  =Interest only 5 year")
        print("productId = 2.69 % p.a.Extra Home Loan 30 % deposit")
        cal = calculator(driver)
        cal.clickCalculatorlink()
        cal.enterLoanAmount(10000)
        cal.enterDuration(10)
        cal.selectRepayType(5)
        cal.selectProductId(0)
        cal.clickCalculateBtn()
        cal.verifyTotalLoanRepayment("$12,324")
        cal.verifyTotalInterestRepayment("$2,324")



