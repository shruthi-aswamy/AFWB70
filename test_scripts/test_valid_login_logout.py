from generic.base_setup import BaseSetup
from pages.login_page import Loginpage
from pages.enter_time_track_page import EnterTimeTrackPage
from generic.excel import Excel
import pytest

class TestValidLoginLogout(BaseSetup):

    @pytest.mark.run(order=3)
    def test_valid_login_logout(self):
        un=Excel.get_data(self.xl_path,"TestValidLoginLogout",2,1)
        pw=Excel.get_data(self.xl_path,"TestValidLoginLogout",2,2)

        login_page=Loginpage(self.driver)
        #1. Enter valid UN
        login_page.set_username(un)
        #2. Enter valid PW
        login_page.set_password(pw)
        #3. Click on login Button
        login_page.click_loginbutton()
        #4. Click on logout Button
        ett=EnterTimeTrackPage(self.driver)
        ett.click_logout_link()
        #5. Verify that login page is displayed
        displayed = login_page.verify_login_page_is_displayed(self.wait)
        assert displayed