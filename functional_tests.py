from selenium import webdriver
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

        #user is invited to  enter a to-do item

        #user entered 'Peacok fur' in the text area

        #user pressed enter, the webpage refreshs, and lines out
        #"1. Peacok fur"

        #anoher text area shows up so that users can enter another to-do item

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
