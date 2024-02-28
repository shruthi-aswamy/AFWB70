from pages.login_page import Loginpage
from generic.base_setup import BaseSetup
from pages.enter_time_track_page import EnterTimeTrackPage
import pytest
from generic.excel import Excel

class TestValidLogin(BaseSetup):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,"TestValidLogin",2,1)
        pw=Excel.get_data(self.xl_path, "TestValidLogin", 2, 2)
            # 1.enter valid un
        login_page = Loginpage(self.driver)
        login_page.set_username(un)
            #2.enter valid pwd
        login_page.set_password(pw)
            #3.click on login button
        login_page.click_loginbutton()
            #4.verify that home page is displayed
        ett_page=EnterTimeTrackPage(self.driver)
        displayed=ett_page.verify_home_page_is_displayed(self.wait)
        assert displayed