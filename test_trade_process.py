import unittest
from selenium import webdriver
from PO.PageObject.login_page import LoginPage
from PO.PageObject.trade_page import TradeProcessForCRO
from PO.TestDatas import globalDatas as comm

class TestTradeProcessCRO(unittest.TestCase):

    def setup(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(comm.base_url)
        self.driver.maximize_window()
        LoginPage(self.driver).login(*comm.user_info)


    def tearDown(self) -> None:
        self.driver.quit()


    def test_buy_CRO(self):

        TradeProcessForCRO(self.driver).buy_CRO()


    def test_sell_CRO(self):
        TradeProcessForCRO(self.driver).sell_CRO()






