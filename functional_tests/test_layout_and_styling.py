from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time
    
class LayoutStylingTest(FunctionalTest):


    def test_layout_and_stying(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        ## Bug in the current geckodriver, need to call it twice to get
        ## actual size
        time.sleep(0.5)
        self.browser.set_window_size(1024, 768)

        # She notices the inputbox is nicely centered
        inputbox = self.get_item_input_box()
        
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

