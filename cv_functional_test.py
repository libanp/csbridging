from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_author_story(self):


        # An employer has asked to see your CV so you go to see what it
        # currently looks like
        self.browser.get('http://localhost:8000/cv')

        with self.subTest(msg='Basic structure'):
            # You know you are in the right place because your name and 'CV' is
            # in the title and header
            self.assertIn('CV: Liban Hannan', self.browser.title)

            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('Liban Hannan (CV)', header_text)

            # You look over the following sections: Contact details, Education,
            # Key Skills, and Employment history
            sections = [tag.text for tag in self.browser.find_elements_by_tag_name('h2')]
            self.assertEqual(
                    sections, ['Contact Details','Education','Key Skills','Employment History']
                    )

        with self.subTest(msg='Add contact detail'):
            # You see that your contact details are missing. Noticing the "Add"
            # button you click it and a box to enter text appears. You enter
            # your student email address lxh349@student.bham.ac.uk
            button = self.browser.find_element_by_id('id_contact_add_detail_button')
            self.assertEqual(button.text, 'Add')
            button.click()
            time.sleep(1)
            # TODO: Hiding/popup will need to be done with CSS and/or JS later

            inputbox = self.browser.find_element_by_id('id_contact_add_detail_input')
            email = 'lxh349@student.bham.ac.uk'
            inputbox.send_keys(email)

            # When you press enter, the page updates and now your new contact
            # details are listed in the correct section
            inputbox.send_keys(Keys.ENTER)
            time.sleep(1)

            contact_details = self.browser.find_element_by_id('id_contact_details_list')
            details = contact_details.find_elements_by_tag_name('li')
            self.assertIn(email, [detail.text for detail in details])


        # You add a second contact detail to the list, your postal address:
        # Edgbaston, Birmingham, B15 2TT, United Kingdom 
        self.fail('Finish the test!')

        # You notice that your entered your email address incorrectly. You
        # notice the "Edit" button which you click and a text box with the
        # entered email appears. You correct the email to
        # lxh348@student.bham.ac.uk. When you hit enter the page updates with
        # the correct email address


if __name__ == '__main__':
    unittest.main(warnings='ignore')
