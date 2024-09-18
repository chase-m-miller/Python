#! python3
# 2048bot.py - This program opens a web browser and automatically plays 2048.

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open 2048 in Firefox and select the <html> tag
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element('tag name', 'html')


while True:
    # Try to find the 'Try again' button, and prompt the user
    # to start another game if it is found.
    try:
        restartButton = browser.find_element('link text', 'Try again')
        # If the game is over, prompt to start another.
        print('Game over. Start another? (y/n): ')
        response = input()
        if response.lower() == 'y':
            restartButton.click()
        else:
            browser.close()
            break

    # Executes as long as the 'Try again' button is not found.
    except selenium.common.exceptions.NoSuchElementException:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.RIGHT)
        continue
