from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver

from .models import Image
import os

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

    def test_upload_file(self):
        self.browser.get(self.live_server_url)
        '''
        image will be uploaded in img_cdn, in the future I should check os.path.exists before submiting form to be sure
        not to overwrite existing file
        '''
        testname = 'test123test123'
        self.browser.find_element_by_name('name').send_keys(testname)
        self.browser.find_element_by_name('image').send_keys(os.getcwd()+"/testimg.jpg")
        self.browser.find_element_by_name('submit').click()

        obj = Image.objects.get(name=testname)

        imgpath = os.path.join(settings.MEDIA_ROOT, str(obj.image))
        self.assertEqual(os.path.exists(imgpath), True)

        # removing image
        os.remove(imgpath)
