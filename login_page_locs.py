# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By

#username,password,login button elements focus
user_input = (By.XPATH, "//input[@class='user_name']")
pwd_input = (By.XPATH, "//input[@class='pwd']")
login_button = (By.XPATH, '//input[@src="/btn_login.gif"]')