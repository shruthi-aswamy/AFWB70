from selenium.webdriver import ChromeOptions
import pytest
from selenium.webdriver import Chrome
# from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeService
s=ChromeService('../driver/chromedriver.exe')
from pyjavaproperties import Properties
from selenium.webdriver import Remote

class BaseSetup:

    @pytest.fixture(autouse=True)
    def precondition(self):
        print('Accessing property file')
        pptobj = Properties()
        pptobj.load(open("./../config.properties"))

        self.xl_path=pptobj['XL_PATH']
        print('XL PATH',self.xl_path)
        # browser=pptobj['BROWSER']
        # browser=browser.lower()
        # print('browser', browser)

        usergrid=pptobj['USERGRID']
        print('user grid',usergrid)
        gridurl=pptobj['GRIDURL']
        print('grid url',gridurl)

        appurl=pptobj['APPURL']
        print('appurl', appurl)
        ito=pptobj['ITO']
        print('ito',ito)
        eto=pptobj['ETO']
        print('eto',eto)

        if usergrid == "yes":
            print('Executing in remote machine')
            self.driver = Remote(command_executor=gridurl, options=ChromeOptions())
        else:
            print('Executing in local machine')
            self.driver = Chrome(service=s)

        print('Enter the url')
        self.driver.get(appurl)
        print('Maximise the window')
        self.driver.maximize_window()
        print('')
        self.driver.implicitly_wait(ito)
        self.wait = WebDriverWait(self.driver, eto)
    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print('Close the browser')
        self.driver.quit()