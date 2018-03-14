import selenium
from selenium import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    #necessary for tests to have places to test, otherwise tests fail
    fixtures = ['test_places']
    #setup the web driver for loading webpages, clicking and typing
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    #destroy the test web driver, db, etc...
    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):

        #load home page
        self.browser.get(self.live_server_url)
        #find input text box
        input_name= self.browser.find_element_by_id('id_name')
        #enter place name
        input_name.send_keys('Denver')
        #find the add button
        add_button = self.browser.find_element_by_id('add-new-place')
        #click it
        add_button.click()

        # got to make this test code wait for page to reload
        # wait for new element to appear on page
        assert "Tokyo" in self.browser.page_source
        assert "New York" in self. browser.page_source
        #Tokyo and NewYork added from fixtures,
        assert 'Denver'in self.browser.page_source
        #Denver added via this test
        
    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Wishlist' in self.browser.title
