
from PO.PageLocators import login_page_locs as loc
from PO.Commom.basepage import Basepage

class LoginPage(Basepage):


    def login(self,username,pwd):
        self.input_text(loc.user_input, username, "input user_name")
        self.input_text(loc.pwd_input, pwd, "input password")
        self.click_element(loc.login_button, "click login button")