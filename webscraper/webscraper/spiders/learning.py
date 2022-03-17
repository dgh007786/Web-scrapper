import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    staleness_of
 
@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()
 
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.crateandbarrel.com/furniture/beds/")
            print(self.driver.title)
            sleep(5)
        def wait_for_page_load(self, timeout=30):
            #Search for the div-id owl-example
            old_page = self.driver.find_element_by_id('owl-example')  
            yield
            WebDriverWait(self.driver, timeout).until(
                staleness_of(old_page)
            )
        
        def test_click_operation(self):
            # Wait for a timeout duration of 10 seconds, after which we perform a CLICK operation
            with self.wait_for_page_load(timeout=10):
                self.driver.find_element_by_link_text('FREE SIGN UP').click()
                print(self.driver.execute_script("return document.readyState"))
