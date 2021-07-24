# -*- coding:utf-8 -*-

from PO.PageLocators import trade_page_locs as loc
from PO.Commom.basepage import Basepage

class TradeProcessForCRO(Basepage):

    def buy_CRO(self):

        self.click_element(loc.CRO_markets,"click CRO MARKETS")

        self.get_element(loc.CROUSDC,"focus on the CROUSDC")
        self.click_element(loc.trade_button,"click the CRO/USDC trade button")
        self.switch_to_iframe(loc.buy_CRO_iframe,"switch to  buy_CRO iframe")

        self.input_text(loc.price,"0.1469","input the price")
        self.input_text(loc.amount,"10","input the amount")
        self.click_element(loc.submit,"click the submit button")
        self.get_element_exists(loc.check_if_scuess,"check wether the element exists or not")



    def sell_CRO(self):
        self.click_element(loc.CRO_markets,"click CRO MARKETS")

        self.get_element(loc.CROUSDC,"focus on the CROUSDC")
        self.click_element(loc.trade_button,"click the  CRO/USDC trade button")
        self.switch_to_iframe(loc.sell_CRO_iframe,"switch to  sell_CRO iframe")
        self.input_text(loc.price,"0.1469","input the price")
        self.input_text(loc.amount,"10","input the amount")
        self.click_element(loc.submit,"click the submit button")
        self.get_element_exists(loc.check_if_scuess,"check wether the element exists or not")


