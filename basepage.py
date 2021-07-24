# -*- coding:utf-8 -*-

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from PO.Commom.logger import GetLog

from selenium.webdriver.support.ui import Select

class Basepage:

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.loger = GetLog()


    def get_element(self,loc,img_name):
        """return the element when finding it"""
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.getScreenShot(img_name)
            logging.exception("********{}fingding{}element fail********".format(img_name,loc))
            raise
        else:
            return ele


    def switch_to_iframe(self,loc,img_name):
        """switch to iframe ，waiting time 20 seconds"""
        try:
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            self.getScreenShot(img_name)
            logging.exception("********{}switch to iframe fail********".format(img_name,loc))
            raise

    def click_element(self,loc,img_name):
        """click element when it visible"""
        self.wait_ele_visible(loc,img_name)
        ele=self.get_element(loc,img_name)
        try:
            ele.click()
        except:
            self.getScreenShot(img_name)
            logging.exception("********{}click{}element fail********".format(img_name,loc))
            raise

    def input_text(self,loc,value,img_name):
        """input content in the input text"""
        self.wait_ele_visible(loc,img_name)
        ele = self.get_element(loc,img_nameue)
        try:
            ele.send_keys(value)
        except:
            self.getScreenShot(img_name)
            logging.exception("********input text fail********")
            raise


    def get_element_exists(self, loc, img_name):
        """check the element is exists or not"""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            self.loger.getlog("********{}exists***********".format(loc))
        except:
            self.getScreenShot(img_name)
            logging.exception("******{}element not exists********".format(loc))
            raise

    def getScreenShot(self,img_name):
        """the failure screenshot saved to this path:/Output/screenshots
        """
        time = self.loger.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/Output/screenshots/%s_%s.png' % (img_name, time)
        self.loger.getlog('********save the failure sreenshot in {}********'.format(image_file))
        self.driver.get_screenshot_as_file(image_file)












