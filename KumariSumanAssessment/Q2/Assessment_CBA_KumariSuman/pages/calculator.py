from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class calculator():
    def __init__(self,driver):
        self.driver = driver

        """Locators"""

        self.calculator_Link = "Repayments calculator"
        self.loanAmount = "amount"
        self.duration = "term"
        self.ddRepay_Type = "interestOnly"
        self.ddProductId = "productId"
        self.btnCalculate = "submit"
        self.Output = "//div[@class='result-container result-visualisation']//h3"
        self.totalloanrepayment = "//div[@class='total col-xs-12 col-sm-6 col-md-12'][1]/p/span[@class='h3']"
        self.totalinterestrepayment = "//div[@class='total col-xs-12 col-sm-6 col-md-12'][2]/p/span[@class='h3']"

    def clickCalculatorlink(self):
        self.driver.find_element_by_link_text(self.calculator_Link).click()

    def enterLoanAmount(self,amount):
        self.driver.find_element_by_id(self.loanAmount).clear()
        self.driver.find_element_by_id(self.loanAmount).send_keys(amount)

    def enterDuration(self,year):
        self.driver.find_element_by_id(self.duration).clear()
        self.driver.find_element_by_id(self.duration).send_keys(year)

    def selectRepayType(self,repayindex):
        Select(self.driver.find_element_by_id(self.ddRepay_Type)).select_by_index(repayindex)


    def selectProductId(self,productIndex):
        Select(self.driver.find_element_by_id(self.ddProductId)).select_by_index(productIndex)



    def clickCalculateBtn(self):
        self.driver.find_element_by_id(self.btnCalculate).click()

    def verifyTotalLoanRepayment(self,TLR):
        totLoanRepay = str(self.driver.find_element_by_xpath(self.totalloanrepayment).text)
        assert totLoanRepay== TLR

    def verifyTotalInterestRepayment(self,TIR):
        totIntrstRepay = str(self.driver.find_element_by_xpath(self.totalinterestrepayment).text)
        assert totIntrstRepay == TIR

