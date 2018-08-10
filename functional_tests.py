from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewvisitorTest(unittest.TestCase):    #Inherit unittest.Testcase
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #user linking to the website
        self.browser.get('http://localhost:8000')

        #user found that 'to-do' is the title of the website
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #user is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                        'Enter a to-do item')

        #user entered 'Peacock feathers' in the text area
        inputbox.send_keys('Buy peacock feathers')

        #user pressed enter, the webpage refreshs, and lines out
        #"1. Peacok fur"
        inputbox.sendkeys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                        any(row.text == '1: Buy peacock feathers' for row in rows)
                )

        #anoher text area shows up so that users can enter another to-do item

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
