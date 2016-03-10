from django.test import LiveServerTestCase
from selenium import webdriver

# Create your tests here.
class UploadFormLiveTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_is_there_a_form(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Upload form', body.text)