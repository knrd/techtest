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

    def test_404_if_image_not_exists(self):
        response = self.client.get(reverse('imageapp:detail', args=('doesnotexists',)))
        self.assertEqual(response.status_code, 404)

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

        """ chceck if image exists """
        imgpath = os.path.join(settings.MEDIA_ROOT, str(obj.image))
        # print imgpath
        self.assertEqual(os.path.exists(imgpath), True)

        """ chceck if image exists and is named by name field """
        imgpath_expected = os.path.join(settings.MEDIA_ROOT, obj.name + "." + str(obj.image).split(".")[-1])
        # print imgpath_expected
        self.assertEqual(os.path.exists(imgpath_expected), True)

        """
        Status on details page
        """
        response = self.client.get(reverse('imageapp:detail', args=(obj.name,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, str(obj.name))

        # removing image
        os.remove(imgpath)
