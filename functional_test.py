from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about new to-do functionality on her favourite website. She
# goes to check it out:
browser.get('http://localhost:8000/superlists')

# She knows she is in the right place from the mention of 'To-Do' in the title
# and header. 
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby is fly-fishing
# and she likes making her own lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item.

# She enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees that the
# site has generated a unique URL for her -- there is some explanitory text to
# that effect

# She visits that URL - her to-do list is still there.

# Satisfied, she foes back to sleep
browser.quit()
