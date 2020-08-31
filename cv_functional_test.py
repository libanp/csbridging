from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def send_to_inputbox_by_id(self, element_id, text, key=Keys.ENTER):
        inputbox = self.browser.find_element_by_id(element_id)
        inputbox.send_keys(text)
        inputbox.send_keys(key)
        time.sleep(1)

    def check_for_entry_list_by_id(self, element_id, text):
        # Doesn't check its in an unordered list
        entry_list = self.browser.find_element_by_id(element_id)
        entries = entry_list.find_elements_by_tag_name('li')
        self.assertNotEqual(entries, [], f"{element_id} produces empty list")
        self.assertIn(text, [entry.text for entry in entries])

    def test_author_story(self):


        # An employer has asked to see your CV so you go to see what it
        # currently looks like
        self.browser.get('http://localhost:8000/cv')

        with self.subTest('Basic structure'):
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

        with self.subTest('Add contact details'):
            # You see that your contact details are missing. Noticing the "Add"
            # button you click it and a box to enter text appears. You enter
            # your student email address lxh349@student.bham.ac.uk
            button = self.browser.find_element_by_id('id_contact_add_detail_button')
            self.assertEqual(button.text, 'Add')
            button.click()
            time.sleep(1)
            # TODO: Hiding/popup will need to be done with CSS and/or JS later

            email = 'lxh349@student.bham.ac.uk'
            self.send_to_inputbox_by_id('id_contact_add_detail_input', email)
            # When you press enter, the page updates and now your new contact
            self.check_for_entry_list_by_id('id_contact_details_list', email)

            # You add a second contact detail to the list, your postal address:
            # Edgbaston, Birmingham, B15 2TT, United Kingdom 
            address = 'Edgbaston, Birmingham, B15 2TT, United Kingdom'
            self.send_to_inputbox_by_id('id_contact_add_detail_input', address)
            self.check_for_entry_list_by_id('id_contact_details_list', address)



        with self.subTest('Add education details'):
            # You enter your A-level results using the available input
            # TODO: looks refactorable
            start = '2003'
            end = '2008'
            qual = 'A-Levels'
            inst = 'Hillcrest Secondary School, Kenya'
            grade = 'AAAB'
            self.send_to_inputbox_by_id('id_education_start', start, Keys.TAB)
            self.send_to_inputbox_by_id('id_education_end', end, Keys.TAB)
            self.send_to_inputbox_by_id('id_education_qual', qual, Keys.TAB)
            self.send_to_inputbox_by_id('id_education_inst', inst, Keys.TAB)
            self.send_to_inputbox_by_id('id_education_grade', grade, Keys.ENTER)

            # Check that the entry is in the education section
            for part in [start, end, qual, inst, grade]:
                self.check_for_entry_list_by_id('id_education_list', part)

        self.fail('Finish the test!')
        #with self.subTest(msg='Add key skills details'):
            # You enter your key skills using the available input
        #    self.send_to_inputbox_by_id('id_skills_input')

        #with self.subTest(msg='Add employment history details'):
            # You enter your employment history using the available input
            
            # You notice that your entered your email address incorrectly. You
            # notice the "Edit" button which you click and a text box with the
            # entered email appears. You correct the email to
            # lxh348@student.bham.ac.uk. When you hit enter the page updates
            # with the correct email address


if __name__ == '__main__':
    unittest.main(warnings='ignore')
