# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By

CRO_markets = (By.PARTIAL_LINK_TEXT,"CRO Markets")

CROUSDC = (By.PARTIAL_LINK_TEXT,"CRO/USDC")

trade_button = ((By.XPATH,"//button[@class='Trade']"))

price = (By.id,"price")

amount =(By.id,"amount")

total = (By.id,"total")

submit =(By.id,"submit")

buy_CRO_iframe=(By.PARTIAL_LINK_TEXT,"Buy CRO")

Sell_CRO_iframe=(By.PARTIAL_LINK_TEXT,"Sell CRO")

check_if_scuess = (By.XPATH,"//div[@class='trade success']")





