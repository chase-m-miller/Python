#! python3
# 2048bot.py - This program opens a web browser and automatically plays 2048.

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element('tag name', 'html')


while True:
    try:
        restartButton = browser.find_element('link text', 'Try again')
        print('Game over. Start another? (y/n): ')
        response = input()
        if response.lower() == 'y':
            restartButton.click()
        else:
            browser.close()
            break
    except selenium.common.exceptions.NoSuchElementException:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.RIGHT)
        continue
