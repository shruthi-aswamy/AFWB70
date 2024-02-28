from generic.base_setup import BaseSetup
from pages.login_page import Loginpage
from generic.excel import Excel
import pytest


class TestInvalidLogin(BaseSetup):

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        un = Excel.get_data(self.xl_path, 'TestInvalidLogin', 2, 1)
        pw = Excel.get_data(self.xl_path,'TestInvalidLogin',2,2)

        login_page=Loginpage(self.driver)
        #1. Enter invalid Login
        login_page.set_username(un)
        #2. Enter invalid Pw
        login_page.set_password(pw)
        #3. Click on login button
        login_page.click_loginbutton()
        #4. Error message should be displayed
        displayed=login_page.verify_err_msg_is_displayed(self.wait)
        assert displayed