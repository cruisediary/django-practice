import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class BlogTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.set_window_size(1024, 768)

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

    def test_blog_app(self):
        self.browser.get('http://127.0.0.1:8000/blog/')

        self.browser.find_element_by_xpath("//*[contains(text(), Blog List)]")


